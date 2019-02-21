#!/Users/yaliyang/anaconda3/bin/python3
# -*- coding: utf-8 -*-

import re

import json

import urllib.request, urllib.parse, urllib.error


show_str= urllib.request.urlopen("https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=all").read(). decode()

show_data=json.loads(show_str)


for obj in show_data:
    for info in obj["showInfo"]:
        UID = obj["UID"]
        category = obj["category"] 
   #     drama = obj["title"]
   #     troupe = obj ["showunit"] (or [“masterunit”] or in “title”)
        locationName = info["locationName"]
   #     *locationdetails = 
    
   #     *city_info = info["location"]
   #     address = info["location"]
   #     datetime_info = info["time"]

        print (category, "+", locationName)
