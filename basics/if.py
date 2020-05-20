# IF ELSE

a = 5
# 5 > 5 = false
if a >= 5:
    print('\nHello a: ', a)

# if else

if a>4:
    print('\n valu of a: ',a)
else:
    print('\nA is less then 4')

# if elif else case
b = 6
if a > b:
    print('\nA is > then b')
elif b < a:
    print('\n B is > thn A')
else:
    print('\n No one big')

# user input
value1 = input('Enter your value = ')
value2 = input('Enter second value = ')

# if value1 > value2: print('\nYes value1 is greater then value2')
print('\nYes value1 is greater then value2') if value1 > value2 else print('\nYes value2 is greater then value1')

print('\nValue1 Greater') if value1 > value2 else print('\nValue1 Less') if value1 < value2  else print('\nvale1 Greater in else')


