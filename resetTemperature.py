#!/usr/bin/env python
# this script is used to reset dummy mini and maxi temperature. It sets the mini and maxi to the actual temp
# crontab run it every day at midnight
# MINI and MAXI devices are feed all day by the lua script catching the device changes of the real thermometer device (see script_device_MinMaxDaily.lua)
import requests
import json

# change the IDx to fit yours
MINI=183
MAXI=184
THERMO=56

paramsTEMP = dict(
   type='command',
   param='udevice',
   idx='',
   nvalue='0',
   svalue=''
)

params = dict (
    type='devices',
    rid=''
)

host='127.0.0.1:8080'
url='http://%s/json.htm' % host

def resetTimer (idx,temp):
    paramsTEMP['idx']=idx
    paramsTEMP['svalue']=temp
    resp = requests.get(url=url, params=paramsTEMP)
    data = json.loads(resp.text)

    
def getTemp (idx):
    params['rid']=idx
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    if 'result' in data :
        return data["result"][0]["Temp"]
        
x = getTemp(THERMO)
resetTimer(MINI,x)
resetTimer(MAXI,x)

    


