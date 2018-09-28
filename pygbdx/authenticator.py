import configparser
import os
import getpass
from os.path import expanduser
from gbdxtools import Interface
Config = configparser.ConfigParser()
username= raw_input("Enter your username: ")
password=getpass.getpass('Enter your password: ')
with open(os.path.join(expanduser("~"),".gbdx-config"),'w') as cfgfile:
    Config.add_section('gbdx')
    Config.set('gbdx','user_name',username)
    Config.set('gbdx','user_password', password)
    Config.write(cfgfile)
    cfgfile.close()
try:
    gbdx=Interface()
    print('Authenticated')
except Exception as e:
    print(e)
