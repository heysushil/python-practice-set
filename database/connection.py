import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="pythondb"
)

mycursor = mydb.cursor()

# CREATE DATABASE
mycursor.execute("CREATE DATABASE IF NOT EXISTS pythondb")

# CREAT USER TABLE
mycursor.execute("CREATE TABLE IF NOT EXISTS user(id int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(200) NULL, course VARCHAR(100) NULL, mobile INT(10) NULL)")


mycursor.execute("CREATE TABLE IF NOT EXISTS education(id int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, userid int(10) NOT NULL,math int(4) NULL,english int(4) NULL,hindi int(4) NULL)")

mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)
