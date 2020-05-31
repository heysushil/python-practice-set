# creating user details
class UserDetails:
    def __init__(self,*details):
        # print(type(details));exit()
        self.name = details[0]
        self.email = details[1]
        self.course = details[2]
        self.timeing = details[3]
        self.mobile = details[4]
        # self.filename = filename

    def userinfo(self):
        print('\n\n')
        userdetail = '''Hello Mr. {0}, your all details are:
            name: {0}
            email: {1}
            course: {2}
            timeing: {3}
            mobile: {4}       
        '''.format(self.name,self.email,self.course,self.timeing,self.mobile)
        # print(userdetail)

        # stroe user detials
        f = open('c:/xampp/htdocs/htmldemo/python-practice-set/excercies/userfiles/'+self.name+'.txt', 'a')
        f.write(userdetail)

        f = open('c:/xampp/htdocs/htmldemo/python-practice-set/excercies/userfiles/'+self.name+'.txt', 'r')
        print('\n\n',f.read())
        f.close()

    # function to read the file
    def writeandreadfile(self):
        f = open('c:/xampp/htdocs/htmldemo/python-practice-set/excercies/userfiles/'+self.filename, 'r')
        print('\n\n',f.read())

# exit()

name = input('Enter your name: ')
email = input('Enter your email: ')
course = input('Enter your course: ')
timeing = input('Enter your timeing: ')
mobile = input('Enter your mobile: ')

details = UserDetails(name,email,course,timeing,mobile)
details.userinfo()


# call object for read file
# filename = input('Enter file name: ')
# filefun = UserDetails(filename)
# filefun.writeandreadfile()