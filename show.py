#!/Users/yaliyang/anaconda3/bin/python3
# -*- coding: utf-8 -*-

import re

import json

import urllib.request, urllib.parse, urllib.error

url = "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=all"

show_str= urllib.request.urlopen(url).read(). decode()

show_data=json.loads(show_str)


for obj in show_data:
    for info in obj["showInfo"]:
        UID = obj["UID"]
        category = obj["category"] 
   #     drama = obj["title"]
   #     troupe = obj ["showunit"] (or [“masterunit”] or in “title”) 戲劇類比較有用 
        locationName = info["locationName"]
   #     *locationdetails =  不一定有，沒有特別規則切不出來，建議直接使用locationName的資訊 
        address = info["location"]
        city_info = address[0:3]
        datetime_info = info["time"]
        date_info= datetime_info[:11]    
        time_info = datetime_info[11:]

        print (time_info)
