# ABOUT TUPLE
'''
IT'S NON CHANGEABLE
USE WITH SMALL BRACKET ()
TUPLE ONLY CHECK COUNT AND INDEX POSTION

ON LIST OR TUPLE WHAT WE HAVE IS:
    INDEX VALUES
    INDEX POSTIONS

    IN LIST WHAT WE DO:
        CREATE NEW LIST
        CHANGE LIST VALUES BY INDEX POSTION
        MODIFY VALUES
        REMOVE VALUES
        DELETE COMPLETE LIST
'''

tupleval = ('PHP','Python','Java','.Net')
print('\n',tupleval)

# HOW TO CHANGE VALUES IN TUPLE 
# CHANGE TUPLE INTO LIST USING TYPE CONVERGION
tupleaslist = list(tupleval)
print('\nConvert the tuple as list: ',type(tupleaslist))
# NEW LIST FOR ADDING
listval = ['HTML','CSS','BS','JS']
# ADDED TO LISTS
newtupleaslist = tuple(tupleaslist + listval)
print('\nChange list to tuple: ',type(newtupleaslist))
print('\nNew tupel values is: ',newtupleaslist)
# FIND THE LENGTH OF TUPLE
print('\nLength of New tuple: ',len(newtupleaslist))

