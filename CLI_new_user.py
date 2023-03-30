import sqlite3

connection = sqlite3.connect('db.sqlite3')

cursor = connection.cursor()
# Prompt the user to enter the username, email, and password
origin = input('''
            Hey friend!  Welcome to EDR, your multi-langual chatbot.
            Do you have an account? 
            1)Yes
            2)No
''')
               
if(origin=="1"):
    from CLI_user import login
    login()
elif(origin=="2"):
    print("Great! Let's sign you up.")
    name = input("Enter your username: ")
    check_sql = "SELECT COUNT(*) FROM users WHERE name = ?"
    cursor.execute(check_sql, (name,))
    result = cursor.fetchone()
    if result[0] > 0:
        print("That username already exists. Please choose a different username.")
        name=input("Enter your username again please: ")
        check_sql = "SELECT COUNT(*) FROM users WHERE name = ?"
        cursor.execute(check_sql, (name,))
        result = cursor.fetchone()
        if result[0] > 0:
            option=input('''Hmm, that user name exits as well.  Perhaps you have an account.  Would you like 
            to:
            1)Go to the Login Page?
            2)Generate a fun, random username?''')
            if(option=="1"):
                from CLI_user import login
                login()
            elif(option=="2"):
                from random_word import RandomWords
                r=RandomWords()
                name=r.get_random_word()
                print(f'Your new username is :{name}')
            # cursor.close()
            # connection.close()

    email = input("Enter your email: ")
    check_sql_email="SELECT COUNT(*) FROM users WHERE email = ?"
    cursor.execute(check_sql_email, (email,))
    result_email = cursor.fetchone()
    # cursor.close()
    if result_email[0] >0:
        print("Looks like you are already have an account, friend!  Please login instead.")
        #this will redirect the cli to the login in area.  
        from CLI_user import login
        login()
        # connection.close()
    password = input("Enter your password: ")

    insert_sql = '''INSERT INTO users (name, email, password)
                        VALUES (?, ?, ?)'''

    cursor.execute(insert_sql, (name, email, password))

    connection.commit()
    print("User added successfully. You are now being redirected to login.")
    from CLI_user import login
    login()
#i would like to open python CLI_users.py after the sign up process is completed
cursor.close()
connection.close()
