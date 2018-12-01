import requests
from dbdb import *


r = requests.get(
    'https://collectionapi.metmuseum.org/public/collection/v1/objects')
countries = []
objectIDs = r.json()["objectIDs"]

for thisid in objectIDs[:int(len(objectIDs)/2)]:
    if thisid <= 9094:
        print(f"skip {thisid}")
        continue
    r = requests.get(
        f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{thisid}')
    thisobject = r.json()
    print(thisid)
    if thisobject["primaryImage"] != "" and thisobject["country"] != "":
        if thisobject["artistBeginDate"] != "" and thisobject["artistEndDate"] != "":
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


# {
#     "title": thisobject["title"],
#     "category": "Art",
#     "yearFrom": int(thisobject["artistBeginDate"]),
#     "yearTo": int(thisobject["artistEndDate"]),
#     "city": thisobject["country"],
#     "image": thisobject["primaryImage"],
#     "detail": [
#         thisobject["classification"], thisobject["period"], thisobject[
#             "constituents"], thisobject["repository"]
#     ],
#     "url": thisobject["objectURL"]
# }

# 一半：236554
