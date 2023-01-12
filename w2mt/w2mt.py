import argparse
import datetime
import os
import re
import sys
import unicodedata

query_template = """[bbox: {}, {}, {}, {}]
[out:json]
[timeout:25]
;
(
	way;
	node;
);
out body;
>;
out skel qt;"""

world_mt_template = """enable_damage = false
creative_mode = true
mod_storage_backend = sqlite3
auth_backend = sqlite3
backend = sqlite3
player_backend = sqlite3
gameid = minetest
world_name = {}
server_announce = false
load_mod_world2minetest = mods/world2minetest"""


def get_args():
	parser = argparse.ArgumentParser(description="Create a minetest world based on openstreetmap data.")
	parser.add_argument('-p', '--project', default="UNNAMED_w2mt_project", help="Project name")
	parser.add_argument('-v', '--verbose', action='store_true', help="Log to console addionally to logfile.")
	parser.add_argument('-q', '--query', type=argparse.FileType("r", encoding="utf-8"), nargs='?', const='project_query', help="File containing a query with Overpass QL, cf. 'https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL'")
	parser.add_argument('-r', '--reuse_query', action='store_true', help="Reuse project-specific query file.")
	parser.add_argument('-a', '--area', type=ascii, help="Decimal coordinates of two opposite corners of desired area, separated by commas: 'lat_1, long_1, lat_2, long_2'")
	parser.add_argument("--output", "-o", type=ascii, help="Output path for map.dat file which is part of the w2mt mod", default="world2minetest/map.dat")
	return parser.parse_args()

# log to console and/or file, depending on verbose flag:
def log(message):
	now = datetime.datetime.now()
	if args.verbose:
		print(f"[w2mt]: {args.project}: {message}")
	# append to logfile:
	with open(log_file, "a") as logfile:
		logfile.write(f"{now} {args.project}: {message}\n")

# convert text to valid filename:
def slugify(text):
	text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
	text = re.sub(r'[^\w\s-]', '', text.lower())
	return re.sub(r'[-\s]+', '-', text).strip('-_')

def check_project_dir():
	# create missing projects dir:
	if not os.path.isdir(project_path):
		log(f"Project dir '{project_path}‘ missing, trying to create it ...")
		os.makedirs(project_path)
		if os.path.isdir(project_path):
			log(f"Project dir '{project_path}‘ created")
		else:
			log(f"Unable to create project dir '{project_path}‘! Check rights!")
			sys.exit("Unable to create missing project dir.")

def prepare_query_file():
	query_string = ""
	if args.reuse_query:
		with open(query_path, 'r') as file:
			query_string = file.read()
			log(f"Reused project QUERY file {query_path}")
	elif args.query:
		with open(args.query, 'r') as file:
			query_string = file.read()
			log(f"Used query file {args.query}")
	elif args.area:
		# Extract and potentially correct the corners of the area as coordinates:
		stripped = args.area.strip().replace(" ", "").replace("'", "").replace("\"", "")
		corners = stripped.split(",")
		north = max(float(corners[0]), float(corners[2]))
		south = min(float(corners[0]), float(corners[2]))
		west = min(float(corners[1]), float(corners[3]))
		east = max(float(corners[1]), float(corners[3]))
		if (east - west > 180.0):
			tmp = east
			east = west
			west = tmp
		# copy the template query file in place and open it
		query_string = query_template.format(south, west, north, east)
		log(f"Query file generated with S: {south}, W: {west}, N: {north}, E: {east}")
	else:
		log(f"Neither query file specified (-q), nor reusing project query file (-r), nor area given (-a). E.g. '52.524023988954376, 13.390914318783942, 52.51004666633488, 13.415739884736942', i.e. South, West, North, East. You can copy these coordinates from google maps for convenience.")
		sys.exit("Area not specified.")
	# Write the file:
	with open(query_path, 'w') as file:
		file.write(query_string)

def perform_query():
	# do the query and store the result in osm.json file:
	cmd = f'wget -q -O {project_path}/osm.json --post-file={query_path} "https://overpass-api.de/api/interpreter" >> {log_file}'
	log(f"Performing query: '{cmd}' ...")
	os.system(cmd)
	log("... done")

def extract_features_from_osm_json():
	osm_path = os.path.join(project_path, "osm.json")
	cmd = f'python3 parse_features_osm.py {osm_path} -o {feature_path} >> {log_file}'
	log(f"Extracting features using this command: '{cmd}' ...")
	os.system(cmd)
	log("... done")

def generate_map_from_features():
	if args.output:
		cmd = f'python3 generate_map.py --features={feature_path} --output={args.output}>> {log_file}'
	else:
		cmd = f'python3 generate_map.py --features={feature_path} >> {log_file}'
	log(f"Generating map using this command: '{cmd}' ...")
	os.system(cmd)
	log("... done")


def copy_mod_in_runtime_dir():
	# check runtime mods dir:
	mt_mods_dir = os.path.join(os.environ["MINETEST_GAME_PATH"], "mods/world2minetest")
	if not os.path.isdir(mt_mods_dir):
		os.makedirs(mt_mods_dir)
		if os.path.isdir(mt_mods_dir):
			log("Directory for world2minetest mod in minetest home did not exist, hence we created it.")
		else:
			log("Failed to create directory for world2minetest mod in minetest home.")
			return
	#
	# copy init.lua to runtime place:
	cmd = f"cp world2minetest/init.lua \"{mt_mods_dir}\"/"
	os.system(cmd)
	log("Copied init.lua file to mods folder for world2minetest in minetest home (runtime location).")
	#
	# copy map.dat to runtime place:
	cmd = f"cp {args.output} \"{mt_mods_dir}\"/"
	os.system(cmd)
	log("Copied map.dat file to mods folder for world2minetest in minetest home (runtime location).")
	#
	# copy mod.conf to runtime place:
	cmd = f"cp world2minetest/mod.conf \"{mt_mods_dir}/\""
	os.system(cmd)
	log("Copied mod.conf file to mods folder for world2minetest in minetest home (runtime location).")


def define_world_for_project():
	# define world for this project:
	world_dir = os.path.join(os.environ["MINETEST_GAME_PATH"], "worlds", args.project)
	if not os.path.isdir(world_dir):
		os.makedirs(world_dir)
		if os.path.isdir(world_dir):
			log(f"Directory for worlds in minetest home did not exist, hence we created it: {world_dir}")
		else:
			log("Failed to create directory for worlds in minetest home.")
			return
	world_mt_string = world_mt_template.format(args.project)
	# Write the file:
	world_file = os.path.join(world_dir, "world.mt").replace("\"", "")
	with open(world_file, 'w') as file:
		file.write(world_mt_string)
	log(f"World.mt file generated: {world_file}.")


######### SCRIPT EXECUTION STARTS HERE: ##############

args = get_args()

# first log starts with the call to this script with all arguments as given:
log_file = "w2mt.log"
call_string=""
for arg in sys.argv:
	call_string += str(arg) + " "
log(call_string )

# check mandatory options:
if not args.project:
	sys.exit("Projectname is mandatory, use -p or --project followed by projectname.")
else:
	args.project = slugify(args.project)

# setup paths:
cwd = os.getcwd()
query_file = "query.osm";
project_path = os.path.join(cwd, "projects", args.project)
query_path = os.path.join(project_path, query_file)
feature_file = "features_osm.json"
feature_path = os.path.join(project_path, feature_file)

check_project_dir()
prepare_query_file()
perform_query()
extract_features_from_osm_json()
generate_map_from_features()
if os.environ["MINETEST_GAME_PATH"]:
	copy_mod_in_runtime_dir()
	define_world_for_project()
else:
	log("Environment variable MINETEST_GAME_PATH not set. In order to manage w2mt mod and worlds you need to set it to the minetest home dir which should contain 'mods' and 'worlds' folders.")


