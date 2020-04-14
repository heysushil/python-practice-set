import connection as con

def user(username,coursename,mobilenumber):
    # insert data into table
    userqeury = "INSERT INTO user(name,course,mobile) VALUES('{}','{}',{})".format(username,coursename,mobilenumber)
    con.mycursor.execute(userqeury)
    con.mydb.commit()

    print("1 record inserted, ID:", con.mycursor.lastrowid)

# user(username=,coursename,mobilenumber)

# GETING INFO BY USER
username = input('Enter your name')
coursename = input('Enter your course name')
mobilenumber = int(input('Enter your mobile number'))

# CALL USER FUNCTION TO PASS USER INFO
user(username,coursename,mobilenumber)
# user('name':'a','course':'b','mobile':'c')
