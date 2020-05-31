import datetime

print(datetime.datetime.today())

import math, json

# print(math.)

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=5, sort_keys=True))
# for i in json.dumps(x):
#     print(i[x])