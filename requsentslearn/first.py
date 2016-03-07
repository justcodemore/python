# __author__ = 'admin'
# -*- coding: utf-8 -*-

import requests

url = "https://api.github.com/some/endpoint"
headers = {'content-type': 'application/json'}
r = requests.get(url=url, headers=headers)
print r.text
print r.url
print r.encoding
# print r.content

print r.status_code
# r.raise_for_status()
