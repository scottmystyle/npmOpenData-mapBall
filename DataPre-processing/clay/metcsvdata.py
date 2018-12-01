# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
from dbdb import *
import pandas as pd

df = pd.read_csv("MetObjects.csv")  # 讀取資料
countries = []

df = df.dropna(subset=['Country', 'Artist Begin Date', 'Artist End Date'])
df = df['Object ID']
df = df[(df > 9094)]
df = df[(df < 712402)]

for thisid in df:
    r = requests.get(
        f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{thisid}')
    thisobject = r.json()
    print(thisid)
    if thisobject["primaryImage"] != "":
        if thisobject["country"] not in countries:
            countries.append(thisobject["country"])
        print(thisobject["artistBeginDate"])
        thisdata = {
            "title": thisobject["title"],
            "category": "Art",
            "yearFrom": int(thisobject["artistBeginDate"]),
            "yearTo": int(thisobject["artistEndDate"]),
            "city": thisobject["country"],
            "image": thisobject["primaryImage"],
            "detail": [
                thisobject["classification"], thisobject["period"], thisobject[
                        "constituents"], thisobject["repository"]
            ],
            "url": thisobject["objectURL"]
        }
        print("==========")
        # save to dbdb
        eventsTable.insert(thisdata)
        # save to dbdb

print("==========")
print("==========")
print("==========")
print(countries)
