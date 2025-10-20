import mysql.connector
from mysql.connector import Error
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ro16#05$99@",
        
    )

    if mydb.is_connected():
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'als_book_store' created successfully! ")

except mysql.connector.Error as e:
    print(f"Failed to connect ot the  database : {e}" )


mycursor.close()
mydb.close()