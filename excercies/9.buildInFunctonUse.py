# use file methods 

class User():
    # global userinfo = 'hello'
    def __init__(self, data):
        self.name = data['name']
        self.course = data['course']

    # show output of the users
    def detail(self):
        userinfo = '''
        Hello Mr. {0}, Welcome to our course.
        Your course details are as follow:
            Name: {0}
            Course: {1}

        Thank You for part of this.\n
        '''.format(self.name, self.course)
        # print(userinfo)
        return userinfo

class Files(User):
    # def __init__(self,filename):
    #     self.filename = filename
        # super.__init__(data)
        
    # create file
    def storInFile(self):
        userinfo = super().detail()
        
        # check file already exists or not
        f = open('c:/xampp/htdocs/htmldemo/python-practice-set/excercies/userfiles/userdetails.txt', 'a')
        # store data inot file
        f.write(userinfo)
        # read file
        readfile = open('c:/xampp/htdocs/htmldemo/python-practice-set/excercies/userfiles/userdetails.txt', 'r')
        print(readfile.read())



# user input
data = {
    'name': input('Enter your name = '),
    'course': input('Enter your course = ')
}

# create object of class
user = User(data)
user.detail()

# child class
filestore = Files(data)
filestore.storInFile()