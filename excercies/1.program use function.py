'''
About class: 
    1. class in python is use to by class keywaord and if wants to inherit parent class properties into child class then need to add the parent class into chil class by the use of function bracket with class keyword.
    2. class in python mendetory to use the constructor to use class's method other wise the class through a error of undefined. so for that in python have __init__ costructe which is use to pass all the arguments to other methods of class.
    3. in default case when creates a constructer in class then the 1st argument is self to create current instance of the arguments then into the construct again assign the getting arguments with self so that thos arguments will pass to the related methods of class. otherwise in python not have direct way to assess the arguments value by calling object's method. in python it will show a error message. on other way say's that the python will follow oop's concept restrictly.
    4. after creating the construct pass all the arguments to the class object and it will pass those arguemtns to the constructer which creates a instence of those arguements then thos arguement by the help of instense accessed by the methods.
    5. also in python when child class need to access the parent class properties then constructer of child class pass the construct values of child class to parent class's construct using parent class name of by using the super keyword in palce of the parent class name to pass the child cunstruer arguments to the parent class's counstructer.
'''

class Parent:
    def __init__(self,name,course):
        self.name = name
        self.course = course

    def printdetails(self):
        print('\nName: {}, Course: {}'.format(self.name,self.course))

# creat sub class
class Student(Parent):
    def __init__(self, name, course, math):
        super().__init__(name, course)
        self.math = math
    def numbers(self):
        if self.math >= '60':
            print('\nCongratulations you have 1st division. Mr. {} your math subject number is {}.'.format(self.name,self.math))
        elif self.math >= '40':
            print('\nCongratulations you have 1st division. Mr. {} your math subject number is {}.'.format(self.name,self.math))

name = input('Enter your name: ')
course = input('Enter your course: ')
math = input('Enter math\'s number: ')

details = Student(name, course,math)
details.printdetails()
details.numbers()