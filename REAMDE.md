First we'll just generate and obtain info from the region we're interested in

osmosis --read-pbf-fast spain-latest.osm.pbf --bounding-polygon file="vilanovailageltru.poly" --write-xml file="vilanova.osm"

We generate the info for the city

osmfilter vilanova.osm --keep="highway=*" --drop-version > vilanovastreets.osm
(If we want non-repetitive info cat vilanovastreets.osm | sort -u | grep name

We generate only parking data map

osmfilter vilanovastreets.osm --keep="parking*=*" -o=parkingvilanova.osm


Once we've done that we can have a little fun:

python3 parse-parkinginfo.py map_data/spain/vilanovastreets.osm -> parking gps data parsed :D
