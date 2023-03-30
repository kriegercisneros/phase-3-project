'''Old bot.py file before linking up google api'''
# from chatterbot import ChatBot

# import sqlite3

# connection = sqlite3.connect('db.sqlite3')

# cursor = connection.cursor()

# def run_bot(user_id, session_id):
# #EDR stands for ExtremeDataRetrieval
#     bot = ChatBot(
#         "EDR",
#         storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
#         logic_adapters=[
#             'chatterbot.logic.MathematicalEvaluation',
#             'chatterbot.logic.TimeLogicAdapter'
#         ],
#         #enable this feature if you want to prevent user conversations posting to statements db
#         # read_only=True,
#         database_uri = 'sqlite:///db.sqlite3')
    
#     chinese_lang_persona = bot.get_response("早上好，你好吗?", persona='Chinese Language')
#     print('Chinese Language:', "早上好，你好吗")

#     english_lang_persona = bot.get_response('What did you do over the weekend?', persona='English Language')
#     print('English Language:', english_lang_persona)

#     spanish_lang_persona = bot.get_response('Buenos días, ¿cómo estás?', persona='Spanish Language')
#     print('Spanish Language:', spanish_lang_persona)

#     option=input('''
#                 What Bot Language Persona would you like to chat with?
#                 1)English
#                 2)Spanish
#                 3)Simplified Chinese
#                 4)Akan
#     ''')


#     exit_conditions = (":q", "quit", "exit")
#     time_commands = ("Time", "What time is it?", "Do you know the time?")
#     insert_sql_sessions = '''INSERT INTO sessions (user_id) VALUES (?)'''
#     insert_sql_user_convos = '''INSERT INTO user_convos (user_id, sessions_id, user_input, bot_response)
#                                 VALUES (?, ?, ?, ?)'''
    
#     session_started = True
#     if(session_id == None):
#         session_started = False

#     while True:
#         if(option == "1"):
#             user_input = input(">>> ")
#             if user_input.lower() in exit_conditions:
#                 print("🤖 Goodbye, human!")
#                 break
#             else:
#                 eng_lang_persona_response = bot.get_response(user_input, persona='English Language')
#                 print('English Language 🤖:', eng_lang_persona_response)
#                 #checks to see if a session has been started to create a new row of sessions
#                 if session_started == False:
#                     cursor.execute(insert_sql_sessions, (user_id,))
#                     print("User session started.")
#                     # fetch the latest session ID
#                     cursor.execute("SELECT MAX(id) FROM sessions")
#                     #this will only run if a new bot instance is running
#                     session_id = cursor.fetchone()[0]
#                     session_started=True
#                     cursor.execute(insert_sql_user_convos, (user_id, session_id, str(user_input), str(eng_lang_persona_response)))
#                     connection.commit()
#         elif(option == "2"):
#             user_input = input(">>> ")
#             if user_input.lower() in exit_conditions:
#                 print("🤖 Goodbye, human!")
#                 break
#             else:
#                 span_lang_persona_response = bot.get_response(user_input, persona='Spanish Language')
#                 print('Spanish Language 🤖:', span_lang_persona_response)
#                 if session_started == False:
#                     cursor.execute(insert_sql_sessions, (user_id,))
#                     print("User session started.")
#                     # fetch the latest session ID
#                     cursor.execute("SELECT MAX(id) FROM sessions")
#                     #this will only run if a new bot instance is running
#                     session_id = cursor.fetchone()[0]
#                     session_started=True
#                 cursor.execute(insert_sql_user_convos, (user_id, session_id, str(user_input), str(span_lang_persona_response)))
#                 connection.commit()
#             print("User Conversation successfully added.")
#     cursor.close()
#     connection.close()
# # run_bot(2,1)




#         # user_input = input(">>> ")
#         # if user_input.lower() in exit_conditions:
#         #     print("🤖 Goodbye, human!")

#         #     break
#         # # elif user_input.lower() in time_commands:
#         # #     response = bot.get_response(user_input)
#         # #     print(f"🤖 {response}")
#         # else:
#         #     bot_response = bot.get_response(user_input)
#         #     print(f"🤖 {bot_response}")
#         #     # execute the sessions query
#         #     if session_started == False:
#         #         cursor.execute(insert_sql_sessions, (user_id,))
#         #         print("User session started.")
#         #         # fetch the latest session ID
#         #         cursor.execute("SELECT MAX(id) FROM sessions")
#         #         #this will only run if a new bot instance is running
#         #         session_id = cursor.fetchone()[0]
#         #         session_started=True
#             # execute the user_convos query
