"""
Extract all objects with an amenity tag from an osm file and list them
with their name and position.
This example shows how geometries from osmium objects can be imported
into shapely using the WKBFactory.
"""
import osmium as o
import sys
import shapely.wkb as wkblib

wkbfab = o.geom.WKBFactory()

class Parking(o.SimpleHandler):

    def print_amenity(amenity, tags, lon, lat):
        name = tags.get('name', '')
        
       # print(tags['parking'])
        #print(tags['parking:lane:right'])
        #print(tags['parking:lane:left'])
        #print(tags['parking:both'])

        #print (tags)

        #if(es_parking(tags)):
        #    print(lon,lat,tags,name)

        if('parking' in tags):
           #print('parkingaaa')
           print("%f %f parking amenity %-15s %s" % (lat, lon, tags['parking'], name))
        if('parking:lane:both' in tags):
           #print('parking both')
           print("%f %f parking both %-15s %s" % (lat, lon, tags['parking:lane:both'], name))
        if('parking:lane:left' in tags):
          # print('parking left')
            print("%f %f parking left %-15s %s" % (lat, lon, tags['parking:lane:left'], name))
        if('parking:lane:right' in  tags):
            #print('parking right')
           print("%f %f parking right %-15s %s" % (lat, lon, tags['parking:lane:right'], name))

    def way(self,n):
        #print (n.tags)
        if is_parking(n.tags):
            #if(len(n.nodes)):
            valueLon = 0
            valueLat = 0 
            i = 0
            #print (n.nodes)
            while i < len(n.nodes) and (valueLon == 0 and valueLat == 0):
                try:
                    valueLon = n.nodes[i].location.lon
                    valueLat = n.nodes[i].location.lat
                    #print (valores)
                    #coordenadas.append(valores[0].lon)
                    #coordenadas.append(valores[1].lat)
                except:
                    i = i + 1
                    continue

            #print(valorLon,valorLat)
            self.print_amenity(n.tags, valueLon, valueLat)


    def node(self, n):
        #print (n.tags)
        if is_parking(n.tags):
            self.print_amenity(n.tags, n.location.lon, n.location.lat)

    def area(self, a):
        #print (a.tags)
        if is_parking(a.tags):
            wkb = wkbfab.create_multipolygon(a)
            poly = wkblib.loads(wkb, hex=True)
            centroid = poly.representative_point()
            self.print_amenity(a.tags, centroid.x, centroid.y)

def is_parking(tags):

	is_parking = False
	if(('parking' in tags) or ('parking:lane:both' in tags) or ('parking:lane:left' in tags) or ('parking:lane:right' in tags)):
		is_parking = True
	return is_parking

def main(osmfile):

    handler = Parking()

    handler.apply_file(osmfile)

    return 0

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python %s <osmfile>" % sys.argv[0])
        sys.exit(-1)

    exit(main(sys.argv[1]))
