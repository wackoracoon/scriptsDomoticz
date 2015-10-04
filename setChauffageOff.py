#!/usr/bin/env python

import requests
import json

# dictionnary with modules names and ID
switches = {
'ROOM1': 1, 
'ROOM2': 2, 
'OFFICE': 3, 
'BATHROOM': 4, 
'LIVINGROOM': 5, 
'KITCHEN': 6}

host='127.0.0.1:8080'
url='http://%s/json.htm' % host

params = dict(     
   type='timers',     
   idx='' )     

paramsDEL = dict(
   type='command',
   param='deletetimer',
   idx=''
)

def removeAllTimers (idx):
   params['idx']=idx
   resp = requests.get(url=url, params=params)
   data = json.loads(resp.text)
   if 'result' in data :
      for k in data["result"] :
         paramsDEL['idx']=k["idx"]
         requests.get(url=url, params=paramsDEL)

for idx in switches.values() :
  removeAllTimers(idx)
