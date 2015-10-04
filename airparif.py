#!/usr/bin/env python

import requests
import json
# add this script to your crontab
# change the id with yours alerts dummy IDX
# you can add a key/value with 'hier':IDX for yesterday value
days = {
	'jour':52,
	'demain':180
}

AIRLEVEL = {
	0: ['tres faible','1'],
	1: ['faible','2'],
	2: ['moyen','3'],
	3: ['eleve','4'],
	4: ['tres eleve','4']

}

#return the air level as define in the dict
def updateAir (value) :
        if int (value) < 25 :
                return 0
        elif int (value) < 50 :
                return 1
        elif int (value) < 75 :
                return 2
	elif int (value) < 100 :
		return 3
        else :
                return 4

# loop for gettings infos
for day,idx in days.items() :
	r = requests.get('http://www.airparif.asso.fr/appli/api/indice?date=%s' % day)
	status=r.status_code
	if status == 200:
		airparif=r.json()
	        globaldict= airparif.get('global')
        	INDICE= str(globaldict.get('indice'))
        	LEVELAIR = updateAir (INDICE)
		url = 'http://localhost:8080/json.htm?type=command&param=udevice&idx=%s&nvalue=%s&svalue=%s' % ( idx ,  AIRLEVEL[LEVELAIR][1], AIRLEVEL[LEVELAIR][0]+" : "+INDICE)
	        r=requests.get(url)
        	if  r.status_code != 200:
                	print "ERROR DOMOTICZ"
	else:
        	print "ERROR AIRPARIF"
