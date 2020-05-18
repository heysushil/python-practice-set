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
# print(newlist)

# ankit personal detail
ankit = ['ankit','python','delhi']

# add mobile number using append
ankit.append('8798798779')

# append hamesa value ko list ke last me add karta hai
ankit.append('delhi')

# pop hamesa list me last value remove karta hai
ankit.pop(3)
print('\nAnkit = ',ankit)

# single value in tupel

singltuple = ('hello python',)
listval = ['hell']
print(type(listval))
print(type(singltuple))


'''
# Set

    1. Set unorder form me hota hai. isko {} se denote karte hai
    2. set union aur intersection ke liye use hota hai
    3. 
'''


'''
# home work
    1. change tuple values. useing casting
    2. usring for loop to print your perstionl information line by line
    3. for loop ka use karke ek tuple me pade tumhare pernal details ko show karna hai iske baad tuple me abni information ko modify kar ke dubara for loop me updated values ko show karan hai.

# Set Home work

    1. ek set banao aur usko print karo 4 bar aur notic karo ki har ek print output me value ka index change hoga
    2. ek set bana ke uske kisi ek index possion ki value ko print karke dekho ki kya output mil raha hai.
    3. ek set banake usko for loop me chala ke outputs print karo.
    4. add multiple values in set uske baad for loop ka use karke print karo.
    5. ek set banao aur usem 4 new values ko ek baar me add karo aur for loop ka use karke print karo. iske baad me 3 value ko remove karo agar wo value set me nahi hai to errro show nahi hona chaiye uske liye kaonsa method user karna hai set ka wo pata karo.
    6. set ke sare method ko ek baar use kar kar ke dekh lo.
'''
