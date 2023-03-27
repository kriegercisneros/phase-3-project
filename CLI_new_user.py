# import sqlite3

# connection = sqlite3.connect('db.sqlite3')

# cursor = connection.cursor()

# # Prompt the user to enter the username, email, and password
# name = input("Enter your username: ")
# email = input("Enter your email: ")
# password = input("Enter your password: ")

# # Define the SQL statement to insert the new user data into the table
# sql = '''INSERT INTO users (name, email, password)
#         VALUES (?, ?, ?)'''

# # Execute the SQL statement with the user data as a tuple
# cursor.execute(sql, (name, email, password))

# connection.commit()

# cursor.close()
# connection.close()

import sqlite3

connection = sqlite3.connect('db.sqlite3')

cursor = connection.cursor()
# Prompt the user to enter the username, email, and password
name = input("Enter your username: ")
check_sql = "SELECT COUNT(*) FROM users WHERE name = ?"
cursor.execute(check_sql, (name,))
result = cursor.fetchone()
if result[0] > 0:
    print("That username already exists. Please choose a different username.")
    cursor.close()
    connection.close()
    exit()

email = input("Enter your email: ")
check_sql_email="SELECT COUNT(*) FROM users WHERE email = ?"
cursor.execute(check_sql_email, (email,))
result_email = cursor.fetchone()
if result_email[0] >0:
    print("Looks like you are already have an account, friend!  Please login instead.")
    #this will redirect the cli to the login in area.  
    cursor.close()
    connection.close()
    exit()
password = input("Enter your password: ")

insert_sql = '''INSERT INTO users (name, email, password)
                    VALUES (?, ?, ?)'''

cursor.execute(insert_sql, (name, email, password))

connection.commit()
print("User added successfully.")

#i would like to open python CLI_users.py after the sign up process is completed
cursor.close()
connection.close()
