import configparser
import requests
import json
import os
import getpass
import csv
from os.path import expanduser
from multipath import shp2cord
from multipath import shp2cordfile
os.chdir(os.path.dirname(os.path.realpath(__file__)))
url = "https://geobigdata.io/catalog/v2/search"
config=configparser.ConfigParser()

def search(path,start,end,limit):
    try:
        config.read(os.path.join(expanduser("~"),".gbdx-config"))
        at=json.loads(config.get('gbdx_token','json'))
        accesstoken=at['access_token']
        start=str(start)+str('T12:00:00.000Z')
        end=str(end)+str('T12:00:00.000Z')
        if os.path.isfile(path):
            cd=shp2cordfile(path)
            payload= {"searchAreaWkt": cd,"startDate": start,"endDate": end,"limit":limit}
            payload=json.dumps(payload)
            headers = {
                'Content-Type': "application/json",
                'Authorization': "Bearer "+accesstoken,
                }
            response = requests.request("POST", url, data=payload, headers=headers).json()
            for key,value in response['stats']['typeCounts'].items():
                print(str(key)+' '+str(value))
        elif os.path.isdir(path):
            ext = [".geojson", ".shp", ".kml", ".json"]
            for things in os.listdir(path):
                if things.endswith(tuple(ext)):
                    cd=shp2cordfile(os.path.join(path,things))
                    print('')
                    print('Searching DG assets for '+str(things))
                    payload= {"searchAreaWkt": cd,"startDate": start,"endDate": end,"types":["DigitalGlobeProduct"],"limit":limit}
                    payload=json.dumps(payload)
                    headers = {
                        'Content-Type': "application/json",
                        'Authorization': "Bearer "+accesstoken,
                        }
                    response = requests.request("POST", url, data=payload, headers=headers).json()
                    for key,value in response['stats']['typeCounts'].items():
                        print(str(key)+' : '+str(value))
    except Exception as e:
        print('access_token not found')
        subprocess.call('python autenticator.py', shell=True)
# search(path=r'C:\Users\samapriya\Box Sync\IUB\Paper Discussions\Deltas Project Edmond NSF 2016\Analysis\Fishnet-Grid\grid_split',start='2016-01-01',end='2018-01-01',limit=125)
