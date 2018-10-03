import configparser
import os
import json
import subprocess
import requests
from os.path import expanduser
config=configparser.ConfigParser()

url = "https://geobigdata.io/auth/v1/validate_token"

def validate():
    try:
        config.read(os.path.join(expanduser("~"),".gbdx-config"))
        at=json.loads(config.get('gbdx_token','json'))
        accesstoken=at['access_token']
        headers = {
        'Authorization': "Bearer "+accesstoken,
        }
        response = requests.request("GET", url, headers=headers).json()
        print('username: '+str(response['username']))
        print('user id: '+str(response['user_id']))
        print('account id: '+str(response['account_id']))
        print('id: '+str(response['id']))
        print('role: '+str(response['role']))
        print('client_id: '+str(response['client_id']))
        print('Account level: '+str(response['account_level']))
    except Exception as e:
        print('access_token not found')
        subprocess.call('python autenticator.py', shell=True)


