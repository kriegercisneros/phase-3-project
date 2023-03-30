import sqlite3

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()
option2=None
def edit_profile(user_id):
    option=input('''
            Update:
            1)username
    ''')
    if(option=="1"):
        option2=input('''
            What would you like to be called?
        ''')
        if(type(option2)==str):
            update = "UPDATE users SET name =? WHERE id =?"
            cursor.execute(update, (option2, user_id))
            connection.commit()
    
            # connection.close()

# edit_profile(2)
    