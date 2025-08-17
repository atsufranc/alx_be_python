# MySQLServer.py
import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server
    connection = mysql.connector.connect(
        host="localhost",   # change if needed
        user="root",        # your MySQL username
        password="password" # your MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")