'''
array
    index array
    associative array
    multidimentional array

list: [] = changabel, dublicalt value acceptaced 
tuple: () = non changabe, dublicalt value acceptaced

dictonaary: {} = key aur values , dublicalt value not acceptaced
set: {} = dublicalt value not acceptaced
'''

# list = inedex array
newlist = ['shubham','ankit','yogesh']
print( newlist)
print('type of newlist ',type(newlist))
# index array wo values ko 0 se index se startka hai
print(newlist[-2])
# index ka range bhi de sakte hai
# range box [] hamesa isme staring and edinting point hota hai
# if 20 < 20
print(newlist[1:])
print(newlist[:2])

newlist[-2] = 'Ankit Raj'
print(newlist[-2])
print(newlist)
# for(i=1; i<5; i++)
# for(initialization; condition; increment / decrement)

for x in newlist:
    print(x)

print(len(newlist))

newlist.append('Tripati')
print(newlist)

del newlist
print(newlist)


'''

'''