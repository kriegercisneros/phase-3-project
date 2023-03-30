#this needs to run as an independent language bot.  
#ORRRRR
#bot.py can run from past_convos, passing in the persona, having persona
#set to NONE by default
    #then, we can check inside bot.py what persona we are trying to use
    #if there are any, route to that file with the given persona. 
    #if there are NONE persona specified, go ahead and run the input
    #option selector for whatever language the person wants to use
    #then proceed as planned, routing to the different files for different
    #persona selectors as planned
from chatterbot import ChatBot
from google.cloud import translate_v2 as translate
import os
import datetime
import sqlite3

connection = sqlite3.connect('db.sqlite3')

cursor = connection.cursor()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/jackiecisneros/Development/code/phase-3/phase-3-project-2/simple_bot_api.json'


def run_chinese_persona(user_id, session_id):
    translate_client = translate.Client()
    persona="Chinese Persona"

    def translate_to_english(text):
        result = translate_client.translate(text, target_language='en')
        return result['translatedText']

    # Define a function to translate text from English to chinese
    def translate_to_chinese(text):
        result = translate_client.translate(text, target_language='zh-CN')
        return result['translatedText']
    
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
        user_input_chinese = input(">>> ")
        user_input_english = translate_to_english(user_input_chinese) 
        if user_input_chinese.lower() in exit_conditions:
            print("🤖 Goodbye, human!")
            break
        elif user_input_english in time_commands:
            print("🤖 The current time is:", datetime.now().strftime("%H:%M"))
        else:
            # Pass the user's input to the English-trained chatbot
            bot_response_english = bot.get_response(user_input_english, persona='Chinese Language')
            # Translate the bot's response from English to chinese
            bot_response_chinese = translate_to_chinese(str(bot_response_english))
            print('Chinese Language 🤖:', bot_response_chinese)
            if session_started == False:
                cursor.execute(insert_sql_sessions, (user_id, persona,))
                print("User session started.")
                # fetch the latest session ID
                cursor.execute("SELECT MAX(id) FROM sessions")
                #this will only run if a new bot instance is running
                session_id = cursor.fetchone()[0]
                session_started=True
            cursor.execute(insert_sql_user_convos, (user_id, session_id, str(user_input_chinese), str(bot_response_chinese)))
            connection.commit()
# run_chinese_persona(1,1)