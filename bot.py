import config
import telebot  # pip install telebot
from telebot import types  # pip install pyTelegramBotAPI
from telegram.ext import *
#from creds import API_KEY

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=['text'])  #commands=['go', 'start'])  # Обработка команды для старта
def echo(message):
    print(message.from_user.username)
    #bot.send_message(message.chat.id, f'{message.}

    if 'Люда' in message.text:
        bot.send_message(message.chat.id, 'Оооо! Да мы уже давно знакомы!')
    else:
        bot.send_message(message.chat.id, message.text)

# постоянное обращение к серверам телеграм, non-stop - не будет останавливаться даже в случае ошибки
bot.polling(non_stop=True)

#def welcome(message):