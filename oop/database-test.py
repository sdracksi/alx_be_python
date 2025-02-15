import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="128.0.10.5",
    user="shad",
    password="root",
    database="my_test_db"
)

print(mydb.get_server_info())