import configparser
import os
import json
import requests
from os.path import expanduser
config=configparser.ConfigParser()
config.read(os.path.join(expanduser("~"),".gbdx-config"))
try:
    at=json.loads(config.get('gbdx_token','json'))
    accesstoken=at['access_token']
except Exception as e:
    print('access_token not found use pygbdx init')

url = "https://geobigdata.io/auth/v1/validate_token"
headers = {
    'Authorization': "Bearer "+accesstoken,
    }
def validate():
    response = requests.request("GET", url, headers=headers).json()
    print('username: '+str(response['username']))
    print('user id: '+str(response['user_id']))
    print('account id: '+str(response['account_id']))
    print('id: '+str(response['id']))
    print('role: '+str(response['role']))
    print('client_id: '+str(response['client_id']))
    print('Account level: '+str(response['account_level']))
