import connection as con

# FETCH ALL DATA FROM USER TABLE
con.mycursor.execute("SELECT u.*,e.* FROM user u LEFT JOIN education e ON e.userid = u.id") # DESC USE TO ORDER BY DESENDING ORDER

# FETCH ALL ROWS BY fetchall() . AND GET RESULT AS LIST
myresult = con.mycursor.fetchall()

# GET ALL DATA LINE BY LINE USING FOR LOOP
for x in myresult:
    print(x)

