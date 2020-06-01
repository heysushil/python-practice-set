def user(*numbers):
    # print(numbers[0][0]); exit()
    sum = numbers[0][0] + numbers[0][1] + numbers[0][2]
    return sum
# call function

number = [4,6,8]

# funciton calll me list pass ki
answer = user(number)
print('\nSum answer: ',answer)

lambdaval = lambda a: a + 10

print('\nLm val: ',lambdaval(5))

def mul(n):
    # print('\nn = ',n); exit()
    return lambda a: a * n


mulval = mul(5)
mulval1 = mul(10)

print('\nMul of lamdab val = ',mulval(10))
print('\nMul of lamdab val = ',mulval1(10))

