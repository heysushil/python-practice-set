# JSON is text, written with JavaScript object notation.

'''
database
    relational
        mysql, sql, oracal, microsoft

    non-relation
        monngo db

Big-Data
Data Science
'''

import json as j

x = "{'name':'anikit','course':'python'}"
print('X old: ',type(x))
y = j.load(x)
print('New x: ',type(y))


'''
HW

1. learn about relational and non-realation database
2. find top 5 realteion database 
3. find top 5 non-realtion databse

'''