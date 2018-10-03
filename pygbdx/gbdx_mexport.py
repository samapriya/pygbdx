import configparser
import requests
import json
import os
import getpass
import subprocess
import csv
from os.path import expanduser
from multipath import shp2cord
from multipath import shp2cordfile
os.chdir(os.path.dirname(os.path.realpath(__file__)))
url = "https://geobigdata.io/catalog/v2/search"
config=configparser.ConfigParser()
config.read(os.path.join(expanduser("~"),".gbdx-config"))

def mxp(path,start,end,limit):
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
                print('Processing '+str(key)+' : '+str(value))
            for items in response['results']:
                cat=items['properties']['catalogID']
                plat=items['properties']['sensorPlatformName']
                los=os.path.split(path)[0]
                print(os.path.join(los,plat))
                if not os.path.exists(os.path.join(los,plat)):
                    os.makedirs(os.path.join(los,plat))
                if not os.path.exists(os.path.join(los,plat,str(cat)+'_'+str(plat)+'.json')):
                    with open(os.path.join(los,plat,str(cat)+'_'+str(plat)+'.json'), 'w') as outfile:
                        json.dump(items['properties'], outfile)
                else:
                    print('File already Exists: SKIPPING')
    except Exception as e:
        print('access_token not found use pygbdx init')
        subprocess.call('python autenticator.py', shell=True)

#mxp(path=r'C:\planet_demo\imja\nola.geojson',start='2016-01-01',end='2018-01-01',limit=125)
