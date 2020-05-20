# DICTONARY - THIS IS A SINLGE LINE COMMENT

'''
THIS IS A MULTILINE COMMENT

        DICTONARY IS SAME AS ASSOCIATIVE ARRAY WHICH HOLDS KEY AND VALUE
        NOT DUBLICATE VALUE

NO  NAME        TELPHONE
1   RAJA        98797978
'''
# print(string_value)

if 3 > 5:
    print('IIm in if')
    print('Im in print body')

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








'''
DIFF B/W 3.5/3.7/3.8 OF PYTHON
DIFF B/W RELATION AND NON-RELATIN DATABASE
'''

# print("hello")

detail = {'name':'ankit','name':'yogesh'} 


