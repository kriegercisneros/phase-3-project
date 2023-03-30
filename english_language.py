from chatterbot import ChatBot
from google.cloud import translate_v2 as translate
import os
import datetime
import sqlite3

connection = sqlite3.connect('db.sqlite3')

cursor = connection.cursor()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/jackiecisneros/Development/code/phase-3/phase-3-project-2/simple_bot_api.json'

def run_english_language(user_id, session_id):
    persona="English Language"
    exit_conditions = (":q", "quit", "exit")
    time_commands = ("Time", "What time is it?", "Do you know the time?")
    insert_sql_sessions = '''INSERT INTO sessions (user_id, persona) VALUES (?, ?)'''
    insert_sql_user_convos = '''INSERT INTO user_convos (user_id, sessions_id, user_input, bot_response)
                                VALUES (?, ?, ?, ?)'''
    
    session_started = True
    if(session_id == None):
        session_started = False

    bot = ChatBot(
        "EDR",
        storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            'chatterbot.logic.MathematicalEvaluation',
            'chatterbot.logic.TimeLogicAdapter'
        ],
        #enable this feature if you want to prevent user conversations posting to statements db
        # read_only=True,
        database_uri = 'sqlite:///db.sqlite3')
    
    while True:
        '''run english file here'''
        user_input = input(">>> ")
        if user_input.lower() in exit_conditions:
            print("🤖 Goodbye, human!")
            break
        elif user_input in time_commands:
            print("🤖 The current time is:", datetime.now().strftime("%H:%M"))
        else:
            eng_lang_persona_response = bot.get_response(user_input, persona='English Language')
            print('English Language 🤖:', eng_lang_persona_response)
            #checks to see if a session has been started to create a new row of sessions
            if session_started == False:
                cursor.execute(insert_sql_sessions, (user_id, persona,))
                print("User session started.")
                # fetch the latest session ID
                cursor.execute("SELECT MAX(id) FROM sessions")
                #this will only run if a new bot instance is running
                session_id = cursor.fetchone()[0]
                session_started=True
                cursor.execute(insert_sql_user_convos, (user_id, session_id, str(user_input), str(eng_lang_persona_response)))
                connection.commit()
# cursor.close()
# connection.close()
