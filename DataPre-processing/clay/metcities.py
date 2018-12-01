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
df = df['Country']
# df = df[(df > 9094)]
# df = df[(df < 712402)]
countries = []
for i in df:
    if i not in countries:
        countries.append(i)
        print(type(i))
print(countries)
print(len(countries))


# {
#     "_id": {
#         "$oid": "5c01545d19d399eb5dc40089"
#     },
#     "name": "新石器時代 大汶口文化",
#     "coordinates": [
#         36.13368,
#         115.65028
#     ],
#     "yearFrom": -4300,
#     "yearTo": -2500
# }


# for thisid in df:
#     r = requests.get(
#         f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{thisid}')
#     thisobject = r.json()
#     print(thisid)
#     if thisobject["primaryImage"] != "":
#         if thisobject["country"] not in countries:
#             countries.append(thisobject["country"])
#         print(thisobject["artistBeginDate"])
#         thisdata = {
#             "title": thisobject["title"],
#             "category": "Art",
#             "yearFrom": int(thisobject["artistBeginDate"]),
#             "yearTo": int(thisobject["artistEndDate"]),
#             "city": thisobject["country"],
#             "image": thisobject["primaryImage"],
#             "detail": [
#                 thisobject["classification"], thisobject["period"], thisobject[
#                         "constituents"], thisobject["repository"]
#             ],
#             "url": thisobject["objectURL"]
#         }
#         print("==========")
#         # save to dbdb
#         eventsTable.insert(thisdata)
#         # save to dbdb

# print("==========")
# print("==========")
# print("==========")
# print(countries)
