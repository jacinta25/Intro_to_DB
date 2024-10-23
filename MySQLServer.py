#connect to mysql server
import mysql.connector
from mysql.connector import Error

try:
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

except mysql.connector.Error as err:
    print(f"Error: {err}")


finally:
    
    if 'mycursor' in locals() and mycursor: 
        mycursor.close()
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
        print("Mysql connection is closed")