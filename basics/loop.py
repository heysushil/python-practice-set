# LOOP'S

# WHILE LOOP
'''
3 PARAMETS
    INITIALIZATION
    CONDTION
    INCREMENT/DECREMENT
'''
# i initialization
i = 1
# condtion
while i < 6:
    # print i value 
  print(i)
#   check condtion if i value 
  if i == 5:
    break
  i += 1

while i < 10:
    # pass
    print(i)
    i += 1
else:
    print('\nI in not less then 10 anymore')

# FOR LOOP
# fruits is a list and holds index values
fruits = ["apple", "banana", "cherry"]
print('\n fruits o index value',fruits[0])
for x in fruits:
  print(x)

for x in fruits:  
  if x == "banana":
    break
  print('\n',x)

for i in range(2,21,2):
    print(i)
else:
  print("Finally finished!")


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
# CHECK DO-WHICL LOOP IN C OR C++
