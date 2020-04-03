# DICTONARY

'''
DICTONARY IS SAME AS ASSOCIATIVE ARRAY WHICH HOLDS KEY AND VALUE
NOT DUBLICATE VALUE
'''

data = {
    'name':'Ankit Raj',
    'course':'Python'
}

print('\nData Info: ',data)

bigdata = {
    'Ankit': {
        'name':'Ankit Raj',
        'course':'Python'
    },
    'Subham': {
        'name':'Subham',
        'course':'Python'
    }
}
print('\nBig Data: ',bigdata)
print('\nSubhams Info: ',bigdata['Subham'])

# USING FORMAT IN PRINT TO SHOW THE RESULT ON NICE WAY
print('\nHi, {}. Welcome to the {} course.'.format(data['name'],data['course']))
print('\nHi, {}. Welcome to the {} course.'.format(bigdata['Subham']['name'],bigdata['Subham']['course']))

'''
HOME WORK
    USING DICTONARY CREATE YOUR PERSONAL INFO ANS SHOW IT USING PRINT WITH FORMAT ON PARAGRAPH WAY
    CREATE DICTORNARY WITH MULTI INO AND SHOW THEM ON PARAGAPH USING PRINT WITH FORMAT

ALSO LEAR IF/ELSE AND WHILE AND FOR LOOP
'''