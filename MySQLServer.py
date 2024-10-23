#connect to mysql server
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "jacinta25",
    password = "condition2030.KE",
    database = "alx_book_store"
)
#create a new database
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")




print("Database 'alx_book_store' created successfully!")


mycursor.close()
mydb.close()