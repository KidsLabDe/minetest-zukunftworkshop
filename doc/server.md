# Verwaltung und Bedienung lokaler Server

Offene Todos:

-[ ] User des docker demons - kingbbq?


## Ordnerstruktur

Minetest liegt im lokalen Ordner:

`/opt/minetest`

Es gibt 2 Installationen, eine für den Tutorial-Teil, eine für den Bau-Teil später.
Beide sind jeweils als Docker-Container angelegt.

## Tutorial-Welt


`/opt/minetest/Tutorial`

### Zurücksetzen der Tutorial Welt

Die Welt kann mit folgendem Befehl auf den initialen Zustand zurückgesetzt werden:

`sudo sh restore.sh`

Damit wird die Welt gelöscht, das `degub.txt` gelöscht, das Logfile, und die Welt aus `/opt/minetest/_vorlagen/Tutorial` in den Container kopiert.
Danach wird der Container neu gestartet und läuft dann mit `docker-compose up` im Consolen-Modus: man sieht wie er startet und alle Aktionen der User.






## Workshop-Welt


`/opt/minetest/minetest-zfn-docker`


### Import der Daten aus OSM





`192.168.88.254:30000`


