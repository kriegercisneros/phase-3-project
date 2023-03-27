import sqlite3

connection = sqlite3.connect('db.sqlite3')

cursor = connection.cursor()

# sql = '''CREATE TABLE users (
#         id INTEGER PRIMARY KEY,
#         name TEXT NOT NULL, 
#         email TEXT NOT NULL,
#         password TEXT NOT NULL);'''

sql = "DELETE FROM users WHERE id = 2"
cursor.execute(sql)

connection.commit()

cursor.close()
connection.close()
