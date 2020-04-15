# IMPORT CLASS.PY FILE TO USE IT'S FUNCTION 
# import Myclass as my   # IT'S IMORT FULL PAGE 
# from Myclass import Myclass as my
# from Myclass import Mathclass as me
from Myclass import Myclass,Mathclass


# create object of Myclass then you access class properties and methods.
newObj = Myclass('Ankit','Subham')
# Now after creating object of Myclass you have permission to access it's properties and methods

newObj.userDetail()

math = Mathclass(50,50,name="Subham")
math.sumofnum()


import platform

x = platform.system()
print(x)

# x = dir(platform)
# for y in x:
#     print(y)


import datetime

x = datetime.datetime.now()
print(x)

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%D"))

'''
HOME WORK
    1. CREATE NEW CLASS WHERE HAVE METHOD WHICH GET USER INFO BY INPUT BUT USE THIS CLASS METHOD ON ANOTHER FILE USEING IMPORT AND PROVIDE USER INPUT FORM SECOND FILE.

    2. CREATE USER REGISTRAION CLASS WHERE HAVE METHODS LIKE ->
        REGISTERATION OF USER
        SHOW USER DETAILS
        MODIFY USER DETAILS
        REMOVE USER DETAILS

        NOTE: ON THE TIME OF REGISTRAION USE DATETIME TO GET CURRENT DATE AND TIME OF REGISTRAION
        ALSO FOR SOVEING 2ND QUESTION USE: 
            LIST -> APPEND/REMOVE/DEL
            DICTONARY




'''