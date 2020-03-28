#!/usr/bin/python

import urllib.request
import json

yourIP = "10.0.0.23"
baseUrl = f"http://{yourIP}:14002/api/dashboard"
detailUrl = f"http://{yourIP}:14002/api/satellite"

def readURL(url):
    req = urllib.request.Request(url)
    r = urllib.request.urlopen(req).read()
    cont = json.loads(r.decode('utf-8'))
    return cont

def getSattelites(satelliteJSON):
    for satellite in satelliteJSON['data']['satellites']:
        getSatelliteInfo(satellite['id'])
        
def getSatelliteInfo(json):
    auditJSON = readURL(detailUrl + "/" + json)
    print(auditJSON['data']['audit'])


    
satellitesJSON = readURL(baseUrl)

satelites = [getSattelites(satellitesJSON)]

# {'totalCount': 4, 'successCount': 4, 'alpha': 4.524381249999999, 'beta': 0, 'score': 1}
# {'totalCount': 288, 'successCount': 288, 'alpha': 19.99999270287266, 'beta': 0, 'score': 1}
# {'totalCount': 15, 'successCount': 15, 'alpha': 11.197466626964683, 'beta': 0, 'score': 1}
# {'totalCount': 19, 'successCount': 19, 'alpha': 12.83028155182915, 'beta': 0, 'score': 1}
# {'totalCount': 14, 'successCount': 14, 'alpha': 10.73417539680493, 'beta': 0, 'score': 1}

# Highest alpha values you can get are 100 for audits and 20 for uptime.
# The audit and uptime reputation is alpha / (alpha + beta)
# Alpha should be as high as possible and beta should be close to 0
# If you are failing audits alpha will decrease and beta will increase.
# If you hit 0.6 you will get paused
