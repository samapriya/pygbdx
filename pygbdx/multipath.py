import geojson
import json
import geopandas as gpd
import os
import sys
os.chdir(os.path.dirname(os.path.realpath(__file__)))
from kml2ee import kml2coord
from shapely.geometry import shape
path=os.path.dirname(os.path.realpath(__file__))
if path not in sys.path:
    sys.path.insert(0, path)

def coord2wkt(coord):
    o = {
   "coordinates": coord,
   "type": "Polygon"}
    geom = shape(o)
    s = json.dumps(o)
    g1 = geojson.loads(s)
    g2 = shape(g1)
    return (str(g2))

def shp2cord(folder):
    for items in os.listdir(folder):
        if items.endswith('.shp'):
            inD = gpd.read_file(os.path.join(folder,items))
            #Reproject to EPSG 4326
            try:
                data_proj = inD.copy()
                data_proj['geometry'] = data_proj['geometry'].to_crs(epsg=4326)
                for items, rows in data_proj.iterrows():
                    return str(rows['geometry'])
            except Exception, e:
                print e
        elif items.endswith('geojson'):
            with open(os.path.join(folder,items)) as aoi:
                aoi_resp = json.load(aoi)
                aoi_geom = aoi_resp['features'][0]['geometry']['coordinates']
                return coord2wkt(aoi_geom)
        elif items.endswith('.json'):
            with open (os.path.join(folder,items)) as aoi:
                aoi_resp=json.load(aoi)
                aoi_geom=aoi_resp['config'][0]['config']['coordinates']
                return coord2wkt(aoi_geom)
        elif items.endswith('.kml'):
            getcoord=kml2coord(os.path.join(folder,items))
            return coord2wkt(getcoord)

def shp2cordfile(items):
    if items.endswith('.shp'):
        inD = gpd.read_file(items)
        #Reproject to EPSG 4326
        try:
            data_proj = inD.copy()
            data_proj['geometry'] = data_proj['geometry'].to_crs(epsg=4326)
            for items, rows in data_proj.iterrows():
                return str(rows['geometry'])
        except Exception, e:
            print e
    elif items.endswith('geojson'):
        with open(items) as aoi:
            aoi_resp = json.load(aoi)
            aoi_geom = aoi_resp['features'][0]['geometry']['coordinates']
            return coord2wkt(aoi_geom)
    elif items.endswith('.json'):
        with open (items) as aoi:
            aoi_resp=json.load(aoi)
            aoi_geom=aoi_resp['config'][0]['config']['coordinates']
            return coord2wkt(aoi_geom)
    elif items.endswith('.kml'):
        getcoord=kml2coord(items)
        return coord2wkt(getcoord)
#shp2cord(folder=r'C:\planet_demo\testmos')

#     o = {
#    "coordinates": [[[23.314208, 37.768469], [24.039306, 37.768469], [24.039306, 38.214372], [23.314208, 38.214372], [23.314208, 37.768469]]],
#    "type": "Polygon"
# }
