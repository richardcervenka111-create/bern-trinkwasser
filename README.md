# Bern Trinkwasser

Alle öffentlichen Brunnen der Stadt Bern auf einer Karte. Ein Tipp zeigt den nächsten Trinkbrunnen mit Fussweg. DE/EN/SK, kein Tracking, Standort bleibt im Gerät.

Live: **https://richardcervenka111-create.github.io/bern-trinkwasser/**

## Warum

Bern hat über hundert öffentliche Brunnen mit Trinkwasser. Wer das weiss, kauft kein Wasser in Plastik und übersteht den Hitzetag. Wer es nicht weiss, sucht. Die Daten sind in OpenStreetMap, aber nicht als „wo ist der nächste, der trinkbar ist“.

## Was sie zeigt

- Grün: Trinkwasser (`drinking_water=yes`), rot: kein Trinkwasser, gelb: unbekannt
- Filter „nur trinkbar“
- „Nächster Brunnen“: Standort, Luftlinie, Link zur Fussroute
- Name, Standortbeschreibung, Rollstuhl, Flasche, wenn in OSM erfasst

## Daten

`fountains.js` ist ein Auszug aus OpenStreetMap (Overpass, Bounding Box Stadt Bern), Stand siehe `FOUNTAINS_META.osm_base`. Lizenz ODbL, © OpenStreetMap-Beitragende. Karte: OSM-Kacheln. Kartenbibliothek Leaflet 1.9.4 von cdnjs mit Integritätsprüfung.

Aktualisieren:

```
curl -s -H 'Accept: application/json' https://overpass-api.de/api/interpreter \
  --data-urlencode 'data=[out:json][timeout:120];(node["amenity"="drinking_water"](46.90,7.37,46.99,7.50);node["amenity"="fountain"](46.90,7.37,46.99,7.50););out body;' \
  -o data/fountains_raw.json
python3 data/build.py
```

Fehlt ein Brunnen oder stimmt „trinkbar“ nicht? Direkt in OpenStreetMap korrigieren, davon haben alle etwas.

## Lizenz

Code MIT. Daten ODbL (OpenStreetMap).
