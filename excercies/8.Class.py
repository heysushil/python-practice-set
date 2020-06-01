class User():
    x = 'hello class in python'

# cret object of class
class1 = User()
print('\nClass1 = ',class1.x)


# class with method

class NewUser():
    # cunstruc in python
    # remeber alwary construct will recive the arguments and crete it's instenct to pass other mehtod of class
    def __init__(hello, name, course):
        hello.n = name
        hello.c = course

    # method
    def user(h):
        print('Welcome to method in class: Hello Mr. {}, Your course is {}'.format(h.n, h.c))


# user input
name = input('Enter your name = ')
course = input('Enter your course = ')

# class objct 
nuser = NewUser(name, course)
nuser.user()