# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
# from chatterbot.trainers import ListTrainer

# business_persona ={
#     'name': 'Pro Bot', 
#     'language': 'en',
#     'tone': 'formal'
# }

# casual_persona = {
# 'name': 'Casual Bot',
# 'language': 'en',
# 'tone': 'informal'
# }
# business = ChatBot(business_persona['name'])
# casual = ChatBot(casual_persona['name'])
# business.train(['business conversations'])
# casual.train(['casual conversations'])

# # Define a function to respond to user input using the appropriate bot
# def respond_to_input(input_text, persona):
#     if persona == business_persona:
#         response = business.get_response(input_text)
#     elif persona == casual_persona:
#         response = casual.get_response(input_text)
#     return response

# persona = business_persona
# response = respond_to_input('Hello, how are you?', persona)
# print(response)

# persona = casual_persona
# response = respond_to_input('What are you up to today?', persona)
# print(response)


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.logic import LogicAdapter

# Create a new chatbot instance
bot = ChatBot(
    'MyBot',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90,
            'persona': 'my_persona'
        }
    ],
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.unescape_html',
        'chatterbot.preprocessors.convert_to_ascii'
    ], 
    read_only=True
)
#This method will return the MultiLogicAdapter instance with the given persona name, if it exists.
def get_persona(self, persona_name):
    for adapter in self.logic.adapters:
        if isinstance(adapter, LogicAdapter) and adapter.persona == persona_name:
            return adapter
    return None


# Train the bot on different persona-specific datasets
humor_trainer = ChatterBotCorpusTrainer(bot)
humor_trainer.train('chatterbot.corpus.english.humor')

casual_trainer = ChatterBotCorpusTrainer(bot)
casual_trainer.train('chatterbot.corpus.english.food')

# Use the bot with different personas
humor_persona = bot.get_persona('humor')
casual_persona = bot.get_persona('casual')

humor_response = humor_persona.get_response('Hi, can you help me with a humor inquiry?')
print('humor:', humor_response)

casual_response = casual_persona.get_response('What did you do over the weekend?')
print('Casual:', casual_response)
