from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

chatbot = ChatBot('chatbot')
trainer = ListTrainer(chatbot=chatbot)
trainer2 = ChatterBotCorpusTrainer(chatbot=chatbot)

database = open('/home/gustavo/workspace/apitelegram/chatbot/training.txt', 'r').readlines()

trainer.train(database)
# trainer2.train("chatterbot.corpus.Portuguese")
trainer2.train("chatterbot.corpus.portuguese.greetings")
trainer2.train("chatterbot.corpus.portuguese.conversations")

print('Type something to begin...')

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input()

        bot_response = chatbot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break