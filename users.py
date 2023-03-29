import sqlite3

connection = sqlite3.connect('db.sqlite3')

cursor = connection.cursor()

# sql = '''CREATE TABLE users (
#         id INTEGER PRIMARY KEY,
#         name TEXT NOT NULL, 
#         email TEXT NOT NULL,
#         password TEXT NOT NULL);'''

# sql = "DROP TABLE sessions"

# sql = '''CREATE TABLE user_convos (
#         id INTEGER PRIMARY KEY, 
#         user_id INTEGER NOT NULL,
#         sessions_id INTEGER NOT NULL, 
#         user_input TEXT NOT NULL, 
#         bot_response TEXT NOT NULL, 
#         FOREIGN KEY(user_id) REFERENCES users(id), 
#         FOREIGN KEY(sessions_id) REFERENCES sessions(id));'''

# sql= '''CREATE TABLE sessions (
#         id INTEGER PRIMARY KEY, 
#         user_id INTEGER NOT NULL, 
#         start DATETIME DEFAULT CURRENT_TIMESTAMP,
#         FOREIGN KEY(user_id) REFERENCES users(id));'''

#SEED DATA THAT WHERE I CAN TRAIN MY CHATBOT USING LIST TRAINER, AND ALSO DELETE THE ENTIRE STATEMENT
#TABLE

# CORPUS_FILE = "chat.txt"
    # delete= "DELETE FROM statement"
    # cursor.execute(delete)
    # connection.commit()
   
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



# cursor.execute(sql)

connection.commit()

cursor.close()
connection.close()
