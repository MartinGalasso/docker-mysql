import mysql.connector

connection = mysql.connector.connect(
    user='root', password='root', host='mysql', port=3306, database='arboles')
print("DB connected")

cursor = connection.cursor()
cursor.execute('SHOW TABLES;')
arboles = cursor.fetchall()
connection.close()
print(arboles)
