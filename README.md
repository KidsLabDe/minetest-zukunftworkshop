

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

n



## Minetest Docker

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


## Geo-Daten Import mit World2Minetest

- Im Verzeichnis "geoimport" liegen alle benötigten Skripte, um die GeoDaten aus OpenstreetMap zu importieren. [Details siehe Anleitung](https://github.com/FlorianRaediker/world2minetest).
- Die Mod "world2minetest" muss installiert werden, d.h. das Verzeichnis "geoimport/world2minetest" muss komplett in das mod-Verzeichnis der Minetest-Installation kopiert werden. 
- Beachtet dabei, dass die Datei "geoimport/world2minetest/map.dat" die importierten Geo-Daten enthält - diese muß also ggf. erneut kopiert werden, wenn ihr die Daten noch einmal importiert.
- Um neu importierte Geodaten in die Welt zu bekommen, müsst ihr in Minetest eine neue Welt anlegen, die mod world2minetest aktivieren und dann die Welt starten. Diesen Vorgang müsst ihr nach jedem Import von Geodaten wiederholen. Manuelle Änderungen an eurer generierten Welt gehen dabei verloren und müssen ggf. gesichert und wieder hergestellt werden.


