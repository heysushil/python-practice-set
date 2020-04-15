import connection as con

sql = "UPDATE user SET name='Ritu' WHERE id=2"

con.mycursor.execute(sql)

con.mydb.commit()

print(con.mycursor.rowcount, "record(s) deleted")
