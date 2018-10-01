#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import os
import shapely.wkt
import shapely.geometry
os.chdir(os.path.dirname(os.path.realpath(__file__)))


# Function to merge geojson into one

def mergeFile(local, dir, output):
    fc = {'type': 'FeatureCollection', 'features': []}
    for items in os.listdir(dir):
        if items.endswith('.geojson'):
            f = open(os.path.join(local, items))
            for line in f:
                obj = json.loads(line)
                fc['features'].extend(obj['features'])

            # print(json.dumps(fc))

            with open(os.path.join(local, str(output)), 'w') as outfile:
                json.dump(fc, outfile)
    print('Combined Geojson Exported at '+str(output))

# Function to extract and convert WKT footprint to geojsons

def fxp(path, dir, output):
    base = {'type': 'FeatureCollection', 'features': [{'type': 'Feature'
            , 'properties': {}, 'geometry': {'type': 'Polygon',
            'coordinates': []}}]}
    fc = {'type': 'FeatureCollection', 'features': []}
    for items in os.listdir(path):
        if items.endswith('.json'):
            f = open(os.path.join(path, items))
            for line in f:
                obj = json.loads(line)
                s = obj['footprintWkt']
                g1 = shapely.wkt.loads(s)
                g2 = shapely.geometry.mapping(g1)
                form = json.dumps(g2)
                a = json.dumps(g2).replace('[[[[', '[[[').replace(']]]]'
                        , ']]]')
                base['features'][0]['geometry']['coordinates'] = \
                    json.loads(a)['coordinates']
                with open(os.path.join(dir, str(items).replace('.json',
                          '.geojson')), 'w') as outfile:
                    json.dump(base, outfile)
    print('Geojson Exports Complete at '+str(dir))
    mergeFile(local=path, dir=dir, output=output)

# fxp(path=r'C:\planet_demo\imja\LANDSAT08', dir=r'C:\planet_demo\imja\ge'
#     , output=r'C:\planet_demo\imja\l8.geojson')
