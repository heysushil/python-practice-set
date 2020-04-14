import connection as con

# FETCH ALL DATA FROM USER TABLE
con.mycursor.execute("SELECT * FROM user WHERE name='Vanshika'")

# FETCH ALL ROWS BY fetchall() . AND GET RESULT AS LIST
myresult = con.mycursor.fetchall()

# fetch one row by betchone()
# myresult = con.mycursor.fetchone(). AND GET RESULT AS TUPLE
print('\n Type: ',type(myresult))

# GET ALL DATA LINE BY LINE USING FOR LOOP
for x in myresult:
    print(x)