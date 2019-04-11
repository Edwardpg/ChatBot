# -*- coding: utf-8 -*-

from chatterbot import ChatBot #chatbot
from chatterbot.trainers import ListTrainer #trainador
import os

#Quando já estiver treinado, podemos passar mais um parâmetro sendo read_only=True
#Assim o ChatBot já entende que não há necessidade de treinamento
bot = ChatBot('Magal_ChatBot', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
trainador = ListTrainer(bot)
trainador.train('chatterbot.corpus.portuguese')

for arq in os.listdir('conversas'):
    chats = open('conversas/' + arq, 'r').readlines()
    trainador.train(chats)

while True:
    requisicao = input('Você: ')

    resposta = bot.get_response(requisicao)
    if float(resposta.confidence) > 0.5:
        print('Bot: ' + str(resposta))
    else:    
        print('Bot: Desculpa ainda não consigo responder essa pergunta')
    