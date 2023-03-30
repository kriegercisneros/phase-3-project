from chatterbot import ChatBot
from google.cloud import translate_v2 as translate
import os
import datetime
import sqlite3

connection = sqlite3.connect('db.sqlite3')

cursor = connection.cursor()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/jackiecisneros/Development/code/phase-3/phase-3-project-2/simple_bot_api.json'

#from google.cloud the translate API.  Client()

def run_bot(user_id, session_id):
    translate_client = translate.Client()

    # Define a function to translate text from targeted lang to to English
    def translate_to_english(text):
        result = translate_client.translate(text, target_language='en')
        return result['translatedText']

    # Define a function to translate text from English to Spanish
    def translate_to_spanish(text):
        result = translate_client.translate(text, target_language='es')
        return result['translatedText']
    
    def translate_to_chinese(text):
        result = translate_client.translate(text, target_language='zh-CN')
        return result['translatedText']
    
    def translate_to_akan(text):
        result = translate_client.translate(text, target_language='ak')
        return result['translatedText']

#EDR stands for ExtremeDataRetrieval
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

    option=input('''
                What Bot Language Persona would you like to chat with?
                1)English
                2)Spanish
                3)Simplified Chinese
                4)Akan
    ''')

    exit_conditions = (":q", "quit", "exit")
    time_commands = ("Time", "What time is it?", "Do you know the time?")
    insert_sql_sessions = '''INSERT INTO sessions (user_id) VALUES (?)'''
    insert_sql_user_convos = '''INSERT INTO user_convos (user_id, sessions_id, user_input, bot_response)
                                VALUES (?, ?, ?, ?)'''
    
    #Logic to test if a session is already made.  If it is not, we will add to the database file
    #to make a new session.  
    session_started = True
    if(session_id == None):
        session_started = False

    while True:
        if(option == "1"):
            '''run english file here'''
            user_input = input(">>> ")
            if user_input.lower() in exit_conditions:
                print("🤖 Goodbye, human!")
                break
            else:
                eng_lang_persona_response = bot.get_response(user_input, persona='English Language')
                print('English Language 🤖:', eng_lang_persona_response)
                #checks to see if a session has been started to create a new row of sessions
                if session_started == False:
                    cursor.execute(insert_sql_sessions, (user_id,))
                    print("User session started.")
                    # fetch the latest session ID
                    cursor.execute("SELECT MAX(id) FROM sessions")
                    #this will only run if a new bot instance is running
                    session_id = cursor.fetchone()[0]
                    session_started=True
                    cursor.execute(insert_sql_user_convos, (user_id, session_id, str(user_input), str(eng_lang_persona_response)))
                    connection.commit()
        elif(option == "2"):
            user_input_spanish = input(">>> ")
            user_input_english = translate_to_english(user_input_spanish) 
            if user_input_spanish.lower() in exit_conditions:
                print("🤖 Goodbye, human!")
                break
            elif user_input_english in time_commands:
                print("🤖 The current time is:", datetime.now().strftime("%H:%M"))
            else:
                # Pass the user's input to the English-trained chatbot
                bot_response_english = bot.get_response(user_input_english, persona='Spanish Language')
                # Translate the bot's response from English to Spanish
                bot_response_spanish = translate_to_spanish(str(bot_response_english))
                print('Spanish Language 🤖:', bot_response_spanish)
                if session_started == False:
                    cursor.execute(insert_sql_sessions, (user_id,))
                    print("User session started.")
                    # fetch the latest session ID
                    cursor.execute("SELECT MAX(id) FROM sessions")
                    #this will only run if a new bot instance is running
                    session_id = cursor.fetchone()[0]
                    session_started=True
                cursor.execute(insert_sql_user_convos, (user_id, session_id, str(user_input_spanish), str(bot_response_spanish)))
                connection.commit()
        elif(option == "3"):
            user_input_chinese = input(">>> ")
            user_input_english = translate_to_english(user_input_chinese) 
            if user_input_chinese.lower() in exit_conditions:
                print("🤖 Goodbye, human!")
                break
            elif user_input_english in time_commands:
                print("🤖 The current time is:", datetime.now().strftime("%H:%M"))
            else:
                # Pass the user's input to the English-trained chatbot
                bot_response_english = bot.get_response(user_input_english, persona='chinese Language')
                # Translate the bot's response from English to chinese
                bot_response_chinese = translate_to_chinese(str(bot_response_english))
                print('chinese Language 🤖:', bot_response_chinese)
                if session_started == False:
                    cursor.execute(insert_sql_sessions, (user_id,))
                    print("User session started.")
                    # fetch the latest session ID
                    cursor.execute("SELECT MAX(id) FROM sessions")
                    #this will only run if a new bot instance is running
                    session_id = cursor.fetchone()[0]
                    session_started=True
                cursor.execute(insert_sql_user_convos, (user_id, session_id, str(user_input_chinese), str(bot_response_chinese)))
                connection.commit()
        elif(option == "4"):
            user_input_akan = input(">>> ")
            user_input_english = translate_to_english(user_input_akan) 
            if user_input_akan.lower() in exit_conditions:
                print("🤖 Goodbye, human!")
                break
            elif user_input_english in time_commands:
                print("🤖 The current time is:", datetime.now().strftime("%H:%M"))
            else:
                # Pass the user's input to the English-trained chatbot
                bot_response_english = bot.get_response(user_input_english, persona='akan Language')
                # Translate the bot's response from English to akan
                bot_response_akan = translate_to_akan(str(bot_response_english))
                print('akan Language 🤖:', bot_response_akan)
                if session_started == False:
                    cursor.execute(insert_sql_sessions, (user_id,))
                    print("User session started.")
                    # fetch the latest session ID
                    cursor.execute("SELECT MAX(id) FROM sessions")
                    #this will only run if a new bot instance is running
                    session_id = cursor.fetchone()[0]
                    session_started=True
                cursor.execute(insert_sql_user_convos, (user_id, session_id, str(user_input_akan), str(bot_response_akan)))
                connection.commit()
            # print("User Conversation successfully added.")
    cursor.close()
    connection.close()
# run_bot(2,1)
