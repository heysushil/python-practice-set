# JSON  
# OTHER SIMILER FORMATIING TO STORE TEXT DATA IS -> HTML, XML, XHTML

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

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

print(json.dumps(x))



'''
HOME WORK
    CREATE CLASS IN WHICH HAVE METHODS WHICH HAVE FOLLOWING WORKS TO DO -
        MEHTOD - INSERT NEW USER DATA IN LIST USING APPEND
        THEN THE LIST VALUE WILL CONVERT INTO JSON 

        ALSO PERFORM THE MODIFY LIST VALUE METHOD AND REMOVE LIST VALUE METHOD
        
'''