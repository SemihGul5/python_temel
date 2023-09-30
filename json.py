# -*- coding: utf-8 -*-

import json

with open("data.json") as users:
    data=json.load(users)
    
    for i in range(5):
        print(data[i]["email"])