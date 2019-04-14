# -*- coding: utf-8 -*-
# Permite escrever no padrão PTBR

from chatterbot import ChatBot #chatbot
from chatterbot.trainers import ListTrainer #trainador
import os #Sistema operacional

#Quando já estiver treinado, podemos passar mais um parâmetro sendo read_only=True
#Assim o ChatBot já entende que não há necessidade de treinamento
bot = ChatBot('Magal_ChatBot', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
#Criamos o Bot passando o nome e seu tipo de treinamento
treinador = ListTrainer(bot) #Passamos o Bot para a lista a ser treinada
treinador.train('chatterbot.corpus.portuguese') #Determina que o treinamento será em Português

for arq in os.listdir('conversas'): #Loop dentro da pasta conversas
    chats = open('conversas/' + arq, 'r').readlines()
    # Abre todos os arquivos dentro da pasta conversas e le todas as linhas que há neles
    treinador.train(chats) #Treina e carrega todas as convesas

while True: #Loop até que seja verdadeira a pergunta e resposta
    requisicao = input('Você: ') #Input do usuário

    resposta = bot.get_response(requisicao) #Output apartir do Input do usuário
    if float(resposta.confidence) > 0.5: #Determina uma porcentagem, se o bot está apto ou não a responder a pergunta
        print('Magal_ChatBot: ' + str(resposta)) #Resposta pois houve uma taxa maior de aptidão proposta
    else:    
        print('Magal_ChatBot: Desculpa ainda não consigo responder essa pergunta') #Informa que ainda não há dados suficiente para responder
    