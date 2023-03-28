from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus

# from CLI_user import user_id

import sqlite3
# import sys

# def run_bot(user_id):
connection = sqlite3.connect('db.sqlite3')

cursor = connection.cursor()

CORPUS_FILE = "chat.txt"

def run_bot(args):
#EDR stands for ExtremeDataRetrieval
    chatbot = ChatBot(
        "EDR",
        storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            'chatterbot.logic.MathematicalEvaluation',
            'chatterbot.logic.TimeLogicAdapter'
        ],
        database_uri = 'sqlite:///db.sqlite3')


    # trainer= ListTrainer(chatbot)
    #this is an example of how to manually train the chatbot
    # trainer.train([
    #     "Hi",
    #     "Welcome, friend!"
    # ])
    # trainer.train([
    #     "Can you help with something today?",
    #     "Of course!  Helping is my favorite :)"
    # ])
    # cleaned_corpus = clean_corpus(CORPUS_FILE)
    # trainer.train(cleaned_corpus)

    # trainer_corpus = ChatterBotCorpusTrainer(chatbot)
    # trainer_corpus.train("chatterbot.corpus.english.greetings", "chatterbot.corpus.english.conversations")

    # user_id = sys.argv[1]
    # from CLI_user import user_id 
    exit_conditions = (":q", "quit", "exit")
    time_commands = ("Time", "What time is it?", "Do you know the time?")
    insert_sql_sessions = '''INSERT INTO sessions (user_id) VALUES (?)'''
    insert_sql_user_convos = '''INSERT INTO user_convos (user_id, sessions_id, user_input, bot_response)
                                VALUES (?, ?, ?, ?)'''
    
    session_started = False
    session_id = None

    while True:
        user_input = input(">>> ")
        if user_input.lower() in exit_conditions:
            print("🤖 Goodbye, human!")

            break
        elif user_input.lower() in time_commands:
            response = chatbot.get_response(user_input)
            print(f"🤖 {response}")
        else:
            bot_response = chatbot.get_response(user_input)
            print(f"🤖 {bot_response}")
            # execute the sessions query
            if not session_started:
                cursor.execute(insert_sql_sessions, (user_id,))
                print("User session started.")
                # fetch the latest session ID
                cursor.execute("SELECT MAX(id) FROM sessions")
                #this will only run if a new bot instance is running
                sessions_id = cursor.fetchone()[0]
                session_started=True
            # execute the user_convos query
            cursor.execute(insert_sql_user_convos, (user_id, sessions_id, str(user_input), str(bot_response)))
            connection.commit()
            print("User Conversation successfully added.")

    cursor.close()
    connection.close()
# run_bot()






# while True:
#     user_input = input(">>> ")
#     if user_input.lower() in exit_conditions:
#         print("🤖 Goodbye, human!")
#         break
#     elif user_input.lower() in time_commands:
#         response = chatbot.get_response(user_input)
#         print(f"🤖 {response}")
#     else:
#         bot_response = chatbot.get_response(user_input)
#         print(f"🤖 {bot_response}")
#         #this is where i need to log the query and response in the sessions table and user_convos table
#         insert_sql_sessions = '''INSERT INTO sessions (user_id)'''
#         sessions_id = "SELECT MAX(id) FROM sessions"
#         insert_sql_user_convos = '''INSERT INTO user_convos (user_id, sessions_id, user_input, bot_response)
#                                     VALUES (?, ?, ?, ?)'''
#         cursor.execute(insert_sql_sessions, (user_id))
#         cursor.execute(insert_sql_user_convos, (user_id, sessions_id, user_input, bot_response))
#         connection.commit()
#         print("Session and User Conversation successfully added.")

# cursor.close()
# connection.close()
