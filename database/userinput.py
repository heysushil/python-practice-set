import connection as con

def user(user_userid,user_math,user_english,user_hindi):
    # insert data into table
    userqeury = "INSERT INTO education(userid,math,english,hindi) VALUES({},{},{},{})".format(user_userid,user_math,user_english,user_hindi)
    con.mycursor.execute(userqeury)
    con.mydb.commit()

    print("1 record inserted, ID:", con.mycursor.lastrowid)

# GETING INFO BY USER
user_userid = int(input('Enter your user_userid:-> '))
user_math = int(input('Enter your user_math:-> '))
user_english = int(input('Enter your user_english:-> '))
user_hindi = int(input('Enter your user_hindi:-> '))


# CALL USER FUNCTION TO PASS USER INFO
user(user_userid,user_math,user_english,user_hindi)
# user('name':'a','course':'b','mobile':'c')
