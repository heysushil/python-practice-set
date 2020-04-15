import connection as con

mycursor = con.mydb.cursor()

sql = "DELETE FROM user WHERE id = 1" # DELETE BY ANY TABEL COULUM NAME

mycursor.execute(sql)

con.mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

# DELETE TABLE USING DROP KEYWORD
sqlTable = "DROP TABLE DEMOuser"
mycursor.execute(sqlTable)
con.mydb.commit()


'''

'''