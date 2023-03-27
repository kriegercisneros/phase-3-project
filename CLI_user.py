import sqlite3

connection = sqlite3.connect('db.sqlite3')

cursor = connection.cursor()

email = input("Enter your email: ")
#Declaring a user_id to equal None so i can set it inside of the if statement and use it as an export to bot.py
user_id = None

check_sql_email="SELECT password FROM users WHERE email = ?"
cursor.execute(check_sql_email, (email,))
result_email = cursor.fetchone()
if result_email is None:
    print("That email is not in our system.")
    cursor.close()
    connection.close()
    exit()
else:
    # Extract the retrieved password from the result
    password = input("Enter your password: ")
    db_password = result_email[0]

    # Compare the entered password with the retrieved password
    if password == db_password:
        name = "SELECT name FROM users WHERE email = email"
        cursor.execute(name)
        result_name= cursor.fetchone()
        print(f"Hello, {name}!")
        #now here is where i want to set foreign key user_id
        user_id = "SELECT id FROM users WHERE email=email"


    else:
        print("Invalid password")
        cursor.close()
        connection.close()
    
