

# Minetest - Zukunftsworkshop

## Packliste

- [ ] WLAN AccessPoints
- [ ] Timer
- [ ] Server

## Server / Laptop

Auf dem Server-Laptop ist alles nötige installiert, um den MineTest-Server lokal ohne Internet zu betreiben.

```shell
cd /opt/minetest/ (pfad noch anpassen)
docker-compose up

```

Nach dem Start ist der Server unter folgender IP / Port erreichbar:

`192.168.88.254:30000`





## Minetest Docker

### Main-Config

in main-config/minetest.conf:

```
default_password = blz
default_privs = interact, student, fly, shout, fast, home
basic_privs = interact, student, fly, shout, fast, home
static_spawnpoint = 180 9 1584 # Setzen pro Welt
time_speed = 72 # 0 - Zeit bleibt stehen
name = Gregor # OP des servers
```

### World.mt

Config-Datei im World Ordner

```
backend = leveldb # vs. SQLite - kleinere Datenbank und performanter, u.u. nicht auf allen Plattformen verfügbar (macOS)
gameid = antigrief # minetest ohne Lava & TNT
world_name = zukunftsnacht # siehe docker-compose.yaml -worldname - das wird gesucht, nicht der Verzeichnisname
server_announce = false # server soll nicht extern veröffentlicht werden
```

### Worldname

- Ist in der world.mt NICHT der Verzeichnisname
- GameID - "nongrief"

## WLAN
- [ ] Es gibt 3 WLAN Router. Diese erstellen für die Zukunftsnacht ein lokales WLAN speziell für MineTest.
- [ ] Warum haben wir uns entschieden ein eigenes WLAN aufzubauen? Auf der einen Seite haben nicht alle Schulen ein WLAN - auch die Internetverbindung ist nicht immer zuverlässig. Hauptgrund ist aber die ablenkungsfreie Umgebung: der Computer ist nur für die Zukunftsnacht - es gibt kein Internet, kein YouTube...
### Zugangsdaten
- [ ] Die 3 Router sind jeweils mit folgenden IPs erreichbar:
- [ ] - 192.168.88.1 - Haupt-Router
  - 192.168.88.2 / .3 - Client-Router

Das Passwort entspricht dem Mentoren-Passwort auf dem Server-Laptop.

# Performance

```max_packets_per_iteration=32096
max_simultaneous_block_sends_per_client = 160
```

Test mit 40 gleichzeitigen Clients erfolgreich:

<img width="882" alt="AP1 - Interface WLANUplink at admin@192 168 88 1 - Webfig v6 47 10 (long-term) on hAP ac^3 (arm) 2022-11-30 15-26-49" src="https://user-images.githubusercontent.com/4609107/204824733-5b0018bf-634c-435a-a97f-b025fe96f29c.png">

## Tipps und Tricks

- Wenn ein Client sich nicht sofort verbindet und bei "Medien..." hängenbleibt, schließen und neu verbinden
- Netzwerkverbingung testen - ping auf Server zeigt grob die zuverlässigkeit!
- Wenn man mit 3 AP arbeitet, verbindung zwischen den AP sicherstellen (siehe WirelessUpLink Signal) - alternativ mit Ethernet Kabeln aus Koffer "Infrastruktur" direkt verbinden.
-


## Import von Geo-Daten mit World2Minetest

- Im Verzeichnis "w2mt" liegen alle benötigten Skripte, um die GeoDaten aus OpenstreetMap zu importieren. [Details siehe Anleitung](https://github.com/FlorianRaediker/world2minetest).
- Wir nutzen aktuell nur die Daten von Openstreetmap und verzichten auf eine Heightmap und Daten von 3D-Modellen.
- Der Ablauf ist grundsätzlich so:
  - Ihr überlegt welchen Bereich der Welt ihr importieren wollt und besorgt euch die Koordinaten von zwei gegenüberliegenden Eckpunkten des Bereichs im Dezimalformat. Das geht zum Beispiel gut auf Google Maps:
	<img width="180" alt="Screenshot 2023-01-11 at 21 27 12" src="https://user-images.githubusercontent.com/19528321/211914444-0cc8ea56-f660-4c50-9e37-18ee4a9ad8bc.png">


  - Ihr wechselt in das Verzeichnis `w2mt` und ruft das script w2mt.py mit dem Projektnamen und den Koordinaten wie folgt auf:

    `python3 w2mt.py -p museumsinsel_berlin -a '52.52337529920812, 13.392572107274946, 52.51061362911302, 13.41347200727846'`
  - Im Projektordner liegen jetzt alle erforderlichen Dateien:

    <img width="611" alt="Screenshot 2023-01-12 at 11 06 00" src="https://user-images.githubusercontent.com/19528321/212038098-8d46212e-cf3a-4728-af68-8bc1a799a4e5.png">

    - `query.osm` - die Anfrage an Openstreetmap mit euren Koordinaten
    - `osm.json` - die von Openstreetmap geladenen Rohdaten
    - `features_osm.json` - extrahierten Geodaten, die in der generierten Welt dargestellt werden


  - Im Homeverzeichnis von Minetest die mod und world Dateien (Voraussetzung dafür ist, dass ihr die Umgebungsvariable `MINETEST_GAME_PATH` so definiert habt, dass sie auf das Homeverzeichnis eurer Minetest Installation zeigt):

    <img width="510" alt="Screenshot 2023-01-12 at 11 18 09" src="https://user-images.githubusercontent.com/19528321/212043634-fc81c5cd-c533-4127-ab99-1c8e80164e16.png">

    - `mods/init.lua` - Startscript für die World2Minetest Mod, das aus den Geodaten die Welt "baut"
    - `mods/map.dat` - Enthält die aus den o.g. Features generierten Voxel (Blöcke)
    - `worlds/<projectname>/world.mt` - Konfiguration der Welt für Minetest


  - Startet minetest und ihr seht die neue Welt in der Liste:

    <img width="829" alt="Screenshot 2023-01-12 at 11 01 04" src="https://user-images.githubusercontent.com/19528321/212037294-eaa4ec9b-ea21-41c5-be21-1d2105d2dfe8.png">



  - Ihr könnt die neue Welt sofort starten, weil die Mod bereits aktiviert ist. Der Spawnpoint ist ca. in der Mitte der Welt.

    <img width="1468" alt="Screenshot 2023-01-12 at 12 12 46" src="https://user-images.githubusercontent.com/19528321/212052200-b63fd50d-84ef-4b4c-9484-8f164b7d3d55.png">


- Weitere Optionen und Infos dazu:
  - In der Datei `w2mt.log` findet ihr ein ausführliches Log über die Importe, die ich durchgeführt habt inkl. Fehlermeldungen.
  - Mit der Option `-v` oder `--verbose` könnt ihr die Log-Infos auch auf der Konsole angezeigt bekommen.
  - Mit der Option `-q` oder `--query` könnt ihr eine eigene Anfragedatei angeben. Lasst dann die Optionen `-r` sowie `-a` oder `--area` weg.
  - Wenn ihr die Anfragedatei, die schon im Projektordner liegt benutzen wollt, gebt die Option `-r` oder `--reuse_query` an.

### python Module

`pip install pyproj numpy scikit-image tqdm matplotlib`

# Ablauf


## Am Morgen

### Preisverleihung

- Gruppenphoto mit allen inkl. Lehrern

### Zettel: wie gehts weiter?

- Zugangsdaten Server
  - Hochladen der Welt direkt
- QR Code für WhatsApp Gruppe oder Insta?
