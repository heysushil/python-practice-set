# FUNCTION

'''
FUNCTION ARE 2 TYPES
    PRE-DEFINED FUNCTION (BUILT-IN FUNCTION)
        THESE FUNCTIONS ARE PRE-PREDFINDED WHICH HAVE A SPECIFIC WORK TO DO.
        THEIR NUMBER OF ARGUMENTS AND RETURN TYPE DEPEND ON THE FUNCTIONS
    USER-DEFINED FUNCTION
        SAME FOR THE USER DEFINED FUNCTION BUT THESE ARE CREATED BY USER
        FUNCTION NAMES AND FUNCTION BODY DEFINED BY USER

FUNCTION BEHAVIOURS
    THESE ARE 4 TYPES
        FUN WITHOUT ARGUMENT AND WITHOUT RETURN VALUE
        FUN WITH    ARGUMENT AND WITH    RETURN VALUE
        FUN WITH    ARGUMENT AND WITHOUT RETURN VALUE
        FUN WITHOUT ARGUMENT AND WIT     RETURN VALUE

IMP POINTS
    ALWAYS PASS SINGLE OR MULTIPLE ARGUMENTS
    BUT RETURN ALWAS SINGLE VALUE
'''

# FUN WITHOUT ARGUMENT AND WITHOUT RETURN VALUE
# DEFINE A FUNCTION
def user():
    print('\nHello Function')

# CALL USER FUNCTION
user()

# FUN WITH    ARGUMENT AND WITHOUT RETURN VALUE
def userWithArg(name,name1):  # RECIVE ANKIT RAJ ARGUMENT IN VARABLE
    print('\nHello, {} and {}. It\'s FUN WITH    ARGUMENT AND WITHOUT RETURN VALUE'.format(name,name1))

userWithArg(name1 = 'Anit Raj',name = 'Shubham') # PASS ONE ARG - ANKIT RAJ

# FUN WITHOUT ARGUMENT AND WIT     RETURN VALUE
def userWithRetrun():
    return '\nHello this is gift from Shubham side';

print(userWithRetrun())

# FUN WITH    ARGUMENT AND WITH    RETURN VALUE
def userWithArgNReturn(name,course,location,mobile):
    return '\nHello, {}, Your course is {} and location is {}. Your contact number is {}.'.format(name,course,location,mobile)

# name = input('Enter Your name: ')
# course = input('Enter YOur course name: ')
# location = input('Your location: ')
# mobile = int(input('Your Mobile: '))
# print(type(mobile))

# subham = userWithArgNReturn(name,course,location,mobile)
# print(subham)
# ankit = userWithArgNReturn('Ankit','Python','India','98788788878')
# print(ankit)

# FUN WHERE GET VALUE BY USER
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

'''
FUNCTION SPECIAL FEATURES
    RECIVE VALUES AS LIST IN CALL BY VALUE LIKE AS: def funname(*arg):
    AT THE TIME OF CALLING FUNCTION, PASS ARGUMENT WITH VARAIABLE NAME BY WHICH YOU CAN RECIVE VALUE ON FUNCTION WITH SPECIFIC VARAIABLE NAME.
'''
# Arbitrary Keyword Arguments, **kwargs SAME LIKE AS DICTONARY
dval = {'name':'ankit'}
print(dval['name'])
# ARBITRARY KEYWORD TO GET VALUES LIKE DICTONARY
def dictonaryFun(**user):
    print('\nValues of user:',user)
    print('\n',type(user))
dictonaryFun(fname='ankit',lname='raj',course='python',mobile='98989898')

# DEFAULT VALUE IN FUNCITON
def my_function(country = "India"):
  print("I am from " + country)

my_function("Sweden")
my_function()
my_function("Brazil")

# PASS LIST
def my_function(a):
    return a + 10
#   for x in food:
    # print(food[x])

# fruits = ["apple", "banana", "cherry"]
# fruits = {'fruit1':'apple','fruit':'banana'}
newfun = my_function(5)

print('\nNewFUn: ',newfun)

# LAMBDA FUN
x = lambda a : a + 10
print(x(5))

# FUNCTIO RECURSION
# def tri_recursion(k):
#     print('\nK value at firs:',k)
#     if(k > 0):
#         print('\nIn if k: ',k)
#         result = k + tri_recursion(k - 1)
#         print('\nRecursion result: ',result)
#     else:
#         result = 0

#     print('\nReturn recursion value: ',result)
#     return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)


'''
HOME WORK
    1. FUNCTION TO PRINT YOUR PERSONAL INFO BY INPUT
    2. FUNCTION TO PRINT PERSONAL DETAIL USEING ARGUMENT AND RETURN VALUE
    3. ADD / SUB / MUL AND DIV WHERE 2 NUMBERS INPUT BY USER AND PERFORM THESE EVENTS
    4. FUNCTION TO CALCULATE AGE

(Don't try to see the solution at first)

Exercise 1
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
    
Exercise 2
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

(Solution - FOLDER-> SOLUTION->INPUT.PY)
'''