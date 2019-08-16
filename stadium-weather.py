#!/usr/bin/env python3

import json
import requests

headers = {'Token': 'hCjRAYvsJWnbzxZKiBLMdLsaZVCuTWlR'}

resp = requests.get(
    ("https://www.ncdc.noaa.gov/cdo-web/api/v2/"
     "locations?locationcategoryid=CITY&"
     "sortfield=name&sortorder=desc&limit=1000"),
    headers=headers
)

data = json.loads(resp.text)['results']
for d in data:
    print(d['name'], d['id'])
