import sqlite3

connection = sqlite3.connect('db.sqlite3')

cursor = connection.cursor()

#welcome back, user!
#what would you like to do?
    #view past conversations
    #start a new conversation BUILD THIS ONE OUT FIRST!!

#starting a new conversation 
    #use user_id from CLI_user.py
    #create a new instance of a session 
    #pulls up the bot.py and uses user input and bot response to populate user_convos and sessions 

