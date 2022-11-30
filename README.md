

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

Test mit 40 gleichzeitigen Clients erfolgreich.


