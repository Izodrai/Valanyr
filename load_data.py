# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 15:29:09 2017

@author: valen
"""

import requests
import time
 
url="http://izo-api-test.azurewebsites.net/api/bids/get_symbol/EURUSD/2017-04-01"
content=requests.get(url)
data=content.json()


if data['Error']['IsAnError'] == True:
    print(data['Error']['MessageError'])
    time.sleep(10)
    quit()

print(data['Bids'])