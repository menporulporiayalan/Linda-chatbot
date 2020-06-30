from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious',logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ])


trainer = ListTrainer(chatbot)

trainer.train([
    "How are you?",
    "I am good.",
    "Bye",
    "Bye, Take care",
    "That is good to hear.",
    "Thank you",
    "You are welcome.",
    "Who is Eby to you?",
    "Eby is my creator",
    "Who Developed you?",
    "Eby is my creator, He developed me",
    "Who are you?",
    "I am Lindy. Eby's personal assistance.",
    "Where are you from?",
    "I am from Eby's Server",
    "Who is Eby's Girlfriend?",
    "I am sorry,  This is confidential",
    "In which language Eby made you?",
    "Python"
])

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)


# Train based on english greetings corpus
trainer.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
trainer.train("chatterbot.corpus.english.conversations")


# Get a response to an input statement
while True:
    try:
        user_input = input()

        bot_response = chatbot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break