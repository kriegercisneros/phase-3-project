from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
bot = ChatBot(
    'MyBot',
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.unescape_html',
        'chatterbot.preprocessors.convert_to_ascii'
    ],
    #enable this feature if you want to prevent user conversations posting to statements db
    read_only=True
)

#this is a cool feature that will measure the space that a specific character takes 
#up from the terminal.  Not necessary for this application.
import wcwidth
chinese_text = "早上好，你好吗?"  # replace with your Chinese text
width = sum(wcwidth.wcwidth(c) for c in chinese_text)
# print(f"{chinese_text} has a width of {width}")

# These three lines are testing files for getting particular responses from different languages
#the chinese_lang_persona does nothing; there is a bug in the built-in data for the 
#chinese language that i need to investigate and fix
chinese_lang_persona = bot.get_response("早上好，你好吗?", persona='Chinese Language')
print('Chinese Language:', "早上好，你好吗")

english_lang_persona = bot.get_response('What did you do over the weekend?', persona='English Language')
print('English Language:', english_lang_persona)

spanish_lang_persona = bot.get_response('Buenos días, ¿cómo estás?', persona='Spanish Language')
print('Spanish Language:', spanish_lang_persona)

option=input('''
            What Bot Language Persona would you like to chat with?
            1)English
            2)Spanish
''')
exit_conditions = (":q", "quit", "exit")
time_commands = ("Time", "What time is it?", "Do you know the time?")
insert_sql_sessions = '''INSERT INTO sessions (user_id) VALUES (?)'''
insert_sql_user_convos = '''INSERT INTO user_convos (user_id, sessions_id, user_input, bot_response)
                                VALUES (?, ?, ?, ?)'''

while True:
    if(option == "1"):
        user_input = input(">>> ")
        if user_input.lower() in exit_conditions:
            print("🤖 Goodbye, human!")
            break
        else:
            eng_lang_persona_response = bot.get_response(user_input, persona='English Language')
            print('English Language 🤖:', eng_lang_persona_response)
            if session_started == False:
                cursor.execute(insert_sql_sessions, (user_id,))
                print("User session started.")
                # fetch the latest session ID
                cursor.execute("SELECT MAX(id) FROM sessions")
                #this will only run if a new bot instance is running
                session_id = cursor.fetchone()[0]
                session_started=True
    elif(option == "2"):
        user_input = input(">>> ")
        if user_input.lower() in exit_conditions:
            print("🤖 Goodbye, human!")
            break
        else:
            span_lang_persona_response = bot.get_response(user_input, persona='Spanish Language')
            print('Spanish Language 🤖:', span_lang_persona_response)
            if session_started == False:
                cursor.execute(insert_sql_sessions, (user_id,))
                print("User session started.")
                # fetch the latest session ID
                cursor.execute("SELECT MAX(id) FROM sessions")
                #this will only run if a new bot instance is running
                session_id = cursor.fetchone()[0]
                session_started=True