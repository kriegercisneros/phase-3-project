import sqlite3

connection = sqlite3.connect('db.sqlite3')

cursor = connection.cursor()

# Prompt the user to enter the username, email, and password
name = input("Enter your username: ")
email = input("Enter your email: ")
password = input("Enter your password: ")

# Define the SQL statement to insert the new user data into the table
sql = '''INSERT INTO users (name, email, password)
        VALUES (?, ?, ?)'''

# Execute the SQL statement with the user data as a tuple
cursor.execute(sql, (name, email, password))

connection.commit()

cursor.close()
connection.close()
