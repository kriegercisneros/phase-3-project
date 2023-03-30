import sqlite3

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

def past_convos(id_from_user):
    session_user_id = "SELECT id FROM sessions WHERE user_id = ?"
    cursor.execute(session_user_id, (id_from_user,))
    #this row returns a list of tuples.  so we need to turn it into a 
    #list comprehension calling each row in our loop
    # session_id= cursor.fetchall()
    session_ids = [row[0] for row in cursor.fetchall()]
    option2=None
    option3=None
    if session_ids ==[]:
         option= input("No conversations yet!  Select 1 to start a new one.")
         if(option == "1"):
            from bot import run_bot
            run_bot(id_from_user, None)
    #session_id = [4, 5, 6, 7, 8]
    else:
        displayed_session_ids =""
        count = 1
        for id in session_ids:
            if count <5:
                displayed_session_ids += (f"{count}: {id}, ")
                count += 1
        option= input(f'''
            Would you like to:
                1) View and Continue a Conversation 
                2) Delete a Conversation     
                    ''')
        if(option =="1"):
            option2 = input(f'''
            Select a conversation to Continue:
                {displayed_session_ids}
            ''')
        else:
            option3 = input(f'''
            Select a conversation to Delete:
                {displayed_session_ids}
            ''')
        #Pulls up the old conversation and then calls bot.py to run the bot again
        if(option2 == "1"):
            session_convos = "SELECT user_input FROM user_convos WHERE sessions_id=?"
            cursor.execute(session_convos, (session_ids[0],))
            user_input = [row[0] for row in cursor.fetchall()]
            # print(f'user_input: {user_input}')

            session_response = "SELECT bot_response FROM user_convos WHERE sessions_id=?"
            cursor.execute(session_response, (session_ids[0],))
            bot_response = [row[0] for row in cursor.fetchall()]
            # print(f'bot_response: {bot_response}')
            for r, resp in zip(user_input, bot_response):
                    print(f'''
                        user: {r}
                            bot: {resp}
                    ''')
            from bot import run_bot
            run_bot(id_from_user, session_ids[0])

        elif(option2 =="2"):
            session_convos = "SELECT user_input FROM user_convos WHERE sessions_id=?"
            cursor.execute(session_convos, (session_ids[1],))
            user_input = [row[0] for row in cursor.fetchall()]
            # print(f'user_input: {user_input}')

            session_response = "SELECT bot_response FROM user_convos WHERE sessions_id=?"
            cursor.execute(session_response, (session_ids[1],))
            bot_response = [row[0] for row in cursor.fetchall()]
            for r, resp in zip(user_input, bot_response):
                    print(f'''
                        user: {r}
                            bot: {resp}
                    ''')

        elif(option2 =="3"):
            session_convos = "SELECT user_input FROM user_convos WHERE sessions_id=?"
            cursor.execute(session_convos, (session_ids[2],))
            user_input = [row[0] for row in cursor.fetchall()]
            # print(f'user_input: {user_input}')

            session_response = "SELECT bot_response FROM user_convos WHERE sessions_id=?"
            cursor.execute(session_response, (session_ids[2],))
            bot_response = [row[0] for row in cursor.fetchall()]
            for r, resp in zip(user_input, bot_response):
                    print(f'''
                        user: {r}
                            bot: {resp}
                    ''')
        elif(option2=="4"):
            session_convos = "SELECT user_input FROM user_convos WHERE sessions_id=?"
            cursor.execute(session_convos, (session_ids[3],))
            user_input = [row[0] for row in cursor.fetchall()]
            # print(f'user_input: {user_input}')
            session_response = "SELECT bot_response FROM user_convos WHERE sessions_id=?"
            cursor.execute(session_response, (session_ids[3],))
            bot_response = [row[0] for row in cursor.fetchall()]
            for r, resp in zip(user_input, bot_response):
                    print(f'''
                        user: {r}
                            bot: {resp}
                    ''')
    #right now i am passing in user id of 4 for testing purposes
    # past_convos(4)

    if(option3 == "1"):
        # print(f"deleting {session_ids[0]}")
        delete= "DELETE FROM sessions WHERE id = ?"
        cursor.execute(delete, (session_ids[0],))
        connection.commit()

    elif(option3 == "2"):
        # print(f"deleting {session_ids[1]}")
        delete= "DELETE FROM sessions WHERE id = ?"
        cursor.execute(delete, (session_ids[1],))
        connection.commit()
    
    elif(option3 == "3"):
        # print(f"deleting {session_ids[2]}")
        delete= "DELETE FROM sessions WHERE id = ?"
        cursor.execute(delete, (session_ids[2],))
        connection.commit()
    
    elif(option3 == "4"):
        # print(f"deleting {session_ids[3]}")
        delete= "DELETE FROM sessions WHERE id = ?"
        cursor.execute(delete, (session_ids[3],))
        connection.commit()
        