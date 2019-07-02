#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import urllib, json
from urllib import request

url = "http://opendata2.epa.gov.tw/AQI.json"
response = request.urlopen(url)
content = response.read()
content = content.decode('utf-8')
data_list = json.loads(content)

for data in data_list:
    for index in data:
        print (index), data[index].encode('utf-8')
print (data_list[0]["SiteName"] + " PM 2.5 is " + data_list[0]["PM2.5"])
