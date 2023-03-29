from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus

import sqlite3

connection = sqlite3.connect('db.sqlite3')

cursor = connection.cursor()

CORPUS_FILE = "chat.txt"

#i want to say if session_id is passed in as an argument, then session_started = True 
#and session_id = session_id
def run_bot(user_id, session_id):
#EDR stands for ExtremeDataRetrieval
    chatbot = ChatBot(
        "EDR",
        storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            'chatterbot.logic.MathematicalEvaluation',
            'chatterbot.logic.TimeLogicAdapter'
        ],
        database_uri = 'sqlite:///db.sqlite3')
    #this is an example of how to manually train the chatbot
    # trainer= ListTrainer(chatbot)
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
    # from CLI_user import select_user_id 
    exit_conditions = (":q", "quit", "exit")
    time_commands = ("Time", "What time is it?", "Do you know the time?")
    insert_sql_sessions = '''INSERT INTO sessions (user_id) VALUES (?)'''
    insert_sql_user_convos = '''INSERT INTO user_convos (user_id, sessions_id, user_input, bot_response)
                                VALUES (?, ?, ?, ?)'''
    
    
    session_started = True
    if(session_id == None):
        session_started = False

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
            if session_started == False:
                cursor.execute(insert_sql_sessions, (user_id,))
                print("User session started.")
                # fetch the latest session ID
                cursor.execute("SELECT MAX(id) FROM sessions")
                #this will only run if a new bot instance is running
                session_id = cursor.fetchone()[0]
                session_started=True
            # execute the user_convos query
            cursor.execute(insert_sql_user_convos, (user_id, session_id, str(user_input), str(bot_response)))
            connection.commit()
            print("User Conversation successfully added.")

    cursor.close()
    connection.close()