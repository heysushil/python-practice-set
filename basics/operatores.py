
x = 5  # assignment operator =
x = 'x'
print(x)

x = 5+5
# x = 10

x += 10 # x = x + 10
print(x)

# agar == 20 to if boday me jayega
# x !=20 to ye else me jayega

if x >= 20:
    print('Yes x is == 20')
else:
    print('No x is not == 20')

# and means aur
name1 = 'raja'
name2 = 'ankit'
if name1 or name2:
    print('Hello '+ name1 + ' and '+name2)

a = 4
b = 4
d = 5
if a != d:
    c = b + 10
    print('value of c ',c)

print('a is b', a is b)