from chatterbot import ChatBot
from google.cloud import translate_v2 as translate
import os
import datetime

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/jackiecisneros/Development/code/phase-3/phase-3-project-2/simple_bot_api.json'

#from google.cloud the translate API.  Client()
translate_client = translate.Client()

# Define a function to translate text from Spanish to English
def translate_to_english(text):
    result = translate_client.translate(text, target_language='en')
    return result['translatedText']

# Define a function to translate text from English to Spanish
def translate_to_akan(text):
    result = translate_client.translate(text, target_language='ak')
    return result['translatedText']

# Create a new ChatBot instance with the English persona
chatbot = ChatBot(
    "My English ChatBot",
    persona={
        'name': 'English Language',
        'engines': [
            'chatterbot.logic.BestMatch',
            'chatterbot.logic.MathematicalEvaluation'
        ]
    }
)
# Define the exit conditions and time commands
exit_conditions = (":q", "quit", "exit")
time_commands = ("Time", "What time is it?", "Do you know the time?")

# Start the conversation loop
while True:
    # Get the user's input in Spanish
    user_input_akan = input(">>> ")

    # Translate the user's input from Spanish to English
    user_input_english = translate_to_english(user_input_akan)

    # Check if the user wants to exit or get the time
    if user_input_english.lower() in exit_conditions:
        print("🤖 Goodbye, human!")
        break
    elif user_input_english in time_commands:
        print("🤖 The current time is:", datetime.now().strftime("%H:%M"))
    else:
        # Pass the user's input to the English-trained chatbot
        bot_response_english = chatbot.get_response(user_input_english)

        # Translate the bot's response from English to Spanish
        bot_response_akan = translate_to_akan(str(bot_response_english))

        # Print the bot's response in Spanish
        print("🤖:", bot_response_akan)
