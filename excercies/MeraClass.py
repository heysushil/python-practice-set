# parent class
class NewClass:
    def __init__(self, name):
        self.name = name
    
    def printName(self):
        print('Welcome to Python\n Hello Mr. {}'.format(self.name))


# child class
class ChildClass(NewClass):
    # concept of overwriteing
    def printName(self):
        print('Hello Print welcome in child class: ')
    def userinfo(self,detail):
        print('Hello Child class')
        print(detail)



# create object of class
# user1 = NewClass(name)
# user1.printName()


'''
Home works
    1. create a file in which store your basic information individualy on variables and then import it in another file where you create a function to print your basic information
    2. then try to create function again but in this case accetp all information varibales on single argument and then print them using fcuntion body.
    3. user your basic info file to use it in class where have 3 methods 1st method use to print only personal info. 2nd mehtod use to print educational info. 3rd method use to print your achivments.
'''