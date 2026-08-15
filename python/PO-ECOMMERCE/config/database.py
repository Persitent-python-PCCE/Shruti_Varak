import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="er@shruti26",
        database="p0_ecommerce"
    )

connection = get_connection()

print("MySQL connection successful!")

connection.close()