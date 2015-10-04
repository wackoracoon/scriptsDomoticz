#!/usr/bin/env python

import requests
import json

# change the IDx to fit yours
ROOM1=1
ROOM2=2
BUREAU=3
BATHROOM=4
LIVINGROOM=5
KITCHEN=5

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

#days = 128 means all days 
paramsADD = dict (
   type='command',
   param='addtimer',
   idx='',
   active='true',
   timertype='2',
   date='',
   hour='',
   min='',
   randomness='false',
   command='',
   level=100,
   hue='0',
   days='128'
)

def removeAllTimers (idx):
   params['idx']=idx
   resp = requests.get(url=url, params=params)
   data = json.loads(resp.text)
   if 'result' in data :
      for k in data["result"] :
         paramsDEL['idx']=k["idx"]
         requests.get(url=url, params=paramsDEL)

# command parameter should be 0 for ON and 1 for OFF
def addTimer(hour,min,command,idx):
   paramsADD['idx']=idx
   paramsADD['hour']=hour
   paramsADD['min']=min
   paramsADD['command']=command
   addData=requests.get(url=url, params=paramsADD)

# for all module, first we remove the existing timers
# then we set the new ones
# in this one the timers will be from 4 to 7 = ON then goes OFF until 15 where it goes ON to 17
removeAllTimers(ROOM1)
addTimer(4,0,0,ROOM1)
addTimer(7,0,1,ROOM1)
addTimer(15,0,0,ROOM1)
addTimer(17,0,1,ROOM1)

removeAllTimers(ROOM2)
addTimer(4,30,0,ROOM2)
addTimer(6,45,1,ROOM2)

removeAllTimers(BUREAU)
addTimer(3,0,0,BUREAU)
addTimer(7,0,1,BUREAU)
addTimer(14,15,0,BUREAU)
addTimer(17,0,1,BUREAU)

removeAllTimers(LIVINGROOM)
addTimer(2,15,0,LIVINGROOM)
addTimer(7,0,1,LIVINGROOM)
addTimer(14,10,0,LIVINGROOM)
addTimer(17,0,1,LIVINGROOM)

removeAllTimers(KITCHEN)
addTimer(2,15,0,KITCHEN)
addTimer(7,0,1,KITCHEN)
addTimer(14,05,0,KITCHEN)
addTimer(17,0,1,KITCHEN)

removeAllTimers(BATHROOM)
addTimer(6,0,0,BATHROOM)
addTimer(8,0,1,BATHROOM)
addTimer(21,0,0,BATHROOM)
addTimer(22,0,1,BATHROOM)




