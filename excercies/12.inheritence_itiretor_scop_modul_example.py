# create class
x = 10

# itertaor
x = [1,2,3,4,5,6]
num = iter(x)
print('\n\nfirst value: ',next(num))
print('value: ',next(num))
print('value: ',next(num))
print('value: ',next(num))
print('value: ',next(num))

# for i in x:
#     print(i)

# fuc
newm = 50
def myfun():
    global newm
    newm = 10
    print('\n\nInner',newm)

myfun()
print('outert: ',newm)

# CLASS IS WORKING ON SAME WAY BUT REMEMBER FEW THINGS WHCIH ALWAS ALSO SAME IN ALL PROGRAMMING LANGAUGES
'''
1. In programming language have facility to include file on oter file so that use the first files concept on next file.
2. Python also provide the by using 'import' by which import and predefined library or modul or also import user defined modules of other files simply.
3. But the main poin here is when we create function or class which is just created and defined one work to do for using them need to call method or create new object in case of class.
4. So same for when import new method be in mind that the method have work but u need to call the method and pass the number of arguments as per method requierments. Also the same in case of class - when trying to use class first need to create a object of the class and then pass the number of agument's then the class work.

Note: At first I was made a mistake here. At first imported the module right way but what I did worng was to not removed the object from that modul whcih I wanted to import so that when I was run that code will produced a error. For that when found the problem then remove the objects form that module and created new objent where I was imported that module. Then the code worked fine.

Also in some case if you are using vs code might show syntex erros because of extensions but work's find. Still I don't know why some time vs code highlight that kind of errors which not affect the code run. But may be occure problems in future that's why showing those syntex or other kind of error's
'''
import MeraClass as mc

# newobj = mc.
# newobj.printName()

# a = MeraClass.printName()

# user input
name = 'Shubham'
# creat object of child class
childObj = mc.ChildClass(name)
childObj.printName()

detail = [1,2,3,4,5,6]
childObj.userinfo(detail)

