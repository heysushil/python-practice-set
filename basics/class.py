# CLASS
'''

'''
class Myclass:
    x = 5
    # _y = 6
    # creating constructer
    def __init__(self, *name):
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

# create object of Myclass then you access class properties and methods.
newObj = Myclass('Ankit','Subham')
# Now after creating object of Myclass you have permission to access it's properties and methods
print(newObj.x)
newObj.user()
newObj.userDetail()

# ANOTHER CLASS
class Mathclass:
    # create cousnstructer and user * for getting values in list form
    def __init__(self,*number):
        self.number = number

    # sum method
    def sumofnum(self):
        print('\nSum of 2 numbers: ',self.number[0]+self.number[1])

    def mulofnum(self):
        print('\nMultiplication of 2 numbers: ',self.number[0] * self.number[1])

# creat object of Mathclass
mathobj = Mathclass(5,10)
mathobj.sumofnum()
mathobj.mulofnum()





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
'''