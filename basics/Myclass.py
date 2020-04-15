# CLASS
'''

'''
class Myclass:
    x = 5
    # _y = 6
    # creating constructer
    def __init__(self, *name):
        print(type(name))
        self.name = name
        # self.name1 = name1
        # print('\nNormal name: ',self.name[0])
        # print('\nObject selef name: ',self.name)
    # creating first method in class
    def user(self):
        print('\nMy noraml functin. Welcome {} and {} '.format(self.name[0],self.name[1]))

    # another functio
    def userDetail(self):
        print('\nHello Mr.{} welcome to the python course.'.format(self.name[0]))

# # create object of Myclass then you access class properties and methods.
# newObj = Myclass('Ankit','Subham')
# # Now after creating object of Myclass you have permission to access it's properties and methods
# print(newObj.x)
# newObj.user()
# newObj.userDetail()

# ANOTHER CLASS
class Mathclass:
    # create cousnstructer and user * for getting values in list form
    def __init__(self,*number,name):
        self.number = number
        self.name = name
        print('\nNew usere: ',self.name)

    # sum method
    def sumofnum(self):
        print('\nSum of 2 numbers: ',self.number[0]+self.number[1])

    def mulofnum(self):
        print('\nMultiplication of 2 numbers: ',self.number[0] * self.number[1])

# GET INPUT BY USER AND USE MATHCLASS TO SUM OF 2 NUMBERS
# inherite THE MATHCLASS
class Userinput(Mathclass):
    # pass
    def __init__(self, *inputs):
        super().__init__(*inputs,name='Default')
    # print('Hello sub class');
    # def user(self):
    #     print('\nSelf values: ',self.number)



# creat object of Mathclass
# pclass = Mathclass(5,10,name='Subham')
# pclass.sumofnum()
# pclass.mulofnum()

# # USERINPUT CLASS OBJECT
# ca = int(input('Enter 1st number'))
# cb = int(input('Enter 2nd number'))
# childclass = Userinput(ca,cb)
# childclass.sumofnum()





'''
HOME WORK
    CREAT CLASS AND SHOW YOUR EDUCATIONS INFO USING PRINT FORMATE IN CLASS METHOD 

    SAME EDUCATIONS INFO WORD THEN PERFORM USING CONSTRUCT IN CLASS THEN PROVIDE ANKIT AND SUBHAM BOTH EDUCATION INFO IN 2 DIFFERENT INPUT CASE

    CREAT CLASS TO PERFORM MATH FUNCTIONS LIKE ADD,SUB,MUL,DIV AT FIRST B/W 2 NUMBERS AND THEN TRY TO CREATE NEW CLASS AND METHOS WITH SAME MATH FUNCTIONS BUT WITH 5 INPUT VALUES

    TRY TO IMPLIMENT INHERITENC IN CLASS


    ABOUT CLASS
        OBJECT
        CONSTRUCT
        DISTRUCT
        ABSTRUCT
        INHERITENCE
        POLIMORPYSIOM
        INCAPSULATION

HOME WORK 2
    1. CREATE CLASS AND IT'S CONSTRUCTER TO SUM AND MUL USING METHOD
    2. CREATE PARENT AND CHILD CLASS TO USE PARENTS PRINT METHOD TO SHOW THE OUTPUT OF CHILD CLASS INPUT METHOD WHERE YOU INPUT USER NAME AND COURSE WHICH YOU PASS TO PARENT CLASS'S PRINT METHOD.
'''