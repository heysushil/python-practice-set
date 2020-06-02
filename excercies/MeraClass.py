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
