import telebot
from telebot import types
from pathlib import Path
import os
import json
import random


bot = telebot.TeleBot('5232368848:AAGba90c8_najQ7eZUL6Nnz0vDCsoaSVCHM')
app_dir = Path(__file__).resolve().parent  # project path
file = os.path.join(app_dir, 'storage.json')


@bot.message_handler(commands=['start'])
def start(message):
    """ Return text from db """
    num = random.randint(0, 16)
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    mess = data['texts'][num]['text']
    markup = types.InlineKeyboardMarkup()
    next_item = types.InlineKeyboardButton('Следующий', callback_data='next')
    stop_item = types.InlineKeyboardButton('Хватит', callback_data='stop')
    markup.add(next_item, stop_item)
    bot.send_message(message.chat.id, mess)
    bot.send_message(message.chat.id, 'Читать следующий анекдот?', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    """ If you press the button next return function start """
    if call.data == 'next':
        start(call.message)
    else:
        bot.send_message(call.message.chat.id, 'До скорого!')


if __name__ == '__main__':
    bot.polling(none_stop=True)
