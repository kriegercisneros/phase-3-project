import sqlite3

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

email = input("Enter your email: ")
#Declaring a user_id to equal None so i can set it inside of the if statement and use it as an export to bot.py
user_id = None
#the question mark is a place holder, where we will supply email during our execute
#this is a sql query that is stored in a variable
check_sql_email="SELECT password FROM users WHERE email = ?"
cursor.execute(check_sql_email, (email,))
#fetchone() returns a tuple containg a single element, which is the password associated with the given email
result_password = cursor.fetchone()
if result_password is None:
    print("That email is not in our system.")
    cursor.close()
    connection.close()
    exit()
else:
    # Extract the retrieved password from the result
    password = input("Enter your password: ")
    db_password = result_password[0]
    # Compare the entered password with the retrieved password
    if password == db_password:
        user_name = "SELECT name FROM users WHERE email = ?"
        cursor.execute(user_name, (email,))
        result_name= cursor.fetchone()
        user_id_query = "SELECT id FROM users WHERE email=?"
        cursor.execute(user_id_query, (email,))
        user_id = cursor.fetchone()[0]
        print(f"Hello, {result_name[0]}!")
        option = input('''
            What would you like to do today?
                1) View and Delete and Continue Past conversations
                2) Start a new conversation 
                3) Edit Profile Information 
            ''')
        if option == "1":
            from past_convos import past_convos
            past_convos(user_id)
            pass
        elif(option=="2"):
            from bot import run_bot
            run_bot(user_id, None)
        elif(option=="3"):
            from edit_profile import edit_profile
            edit_profile(user_id)
            pass
    else:
        print("Invalid password")
        cursor.close()
        connection.close()