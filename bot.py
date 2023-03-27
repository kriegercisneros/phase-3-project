from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus

CORPUS_FILE = "chat.txt"

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


exit_conditions = (":q", "quit", "exit")
time_commands = ("Time", "What time is it?", "Do you know the time?")
while True:
    query = input("Your turn, human: ")
    if query.lower() in exit_conditions:
        print("🤖 Goodbye, human!")
        break
    elif query.lower() in time_commands:
        response = chatbot.get_response(query)
        print(f"🤖 {response}")
    else:
        response = chatbot.get_response(query)
        print(f"🤖 {response}")

    # query = input("Your turn, human: ")
    # if query in exit_conditions:
    #     break
    # else:
    #     print(f"🤖 {chatbot.get_response(query)}")