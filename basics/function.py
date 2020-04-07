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

userWithArg('Anit Raj','Shubham') # PASS ONE ARG - ANKIT RAJ

# FUN WITHOUT ARGUMENT AND WIT     RETURN VALUE
def userWithRetrun():
    return '\nHello this is gift from Shubham side';

print(userWithRetrun())

# FUN WITH    ARGUMENT AND WITH    RETURN VALUE
def userWithArgNReturn(name,course,location,mobile):
    return '\nHello, {}, Your course is {} and location is {}. Your contact number is {}.'.format(name,course,location,mobile)

name = input('Enter Your name: ')
course = input('Enter YOur course name: ')
location = input('Your location: ')
mobile = input('Your Mobile: ')

subham = userWithArgNReturn(name,course,location,mobile)
print(subham)
# ankit = userWithArgNReturn('Ankit','Python','India','98788788878')
# print(ankit)

# FUN WHERE GET VALUE BY USER


'''
HOME WORK
    1. FUNCTION TO PRINT YOUR PERSONAL INFO BY INPUT
    2. FUNCTION TO PRINT PERSONAL DETAIL USEING ARGUMENT AND RETURN VALUE
    3. ADD / SUB / MUL AND DIV WHERE 2 NUMBERS INPUT BY USER AND PERFORM THESE EVENTS
    4. FUNCTION TO CALCULATE AGE
    
'''