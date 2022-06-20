from email import message
import telebot
from config import token_tg
from requests import get
from main import get_weather
from telebot import types
bot=telebot.TeleBot(token_tg)


@bot.message_handler(commands=['start'])
def start(message, res=False):
    sti=open('static/hello.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id,f'Привет, {message.from_user.first_name}!\nЯ бот {bot.get_me().first_name}, я создан в учебных целях.')
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton('Екатеринбург')
    item2=types.KeyboardButton('Челябинск')
    item3 = types.KeyboardButton('Пермь')
    item4 = types.KeyboardButton('Тюмень')
    item5 = types.KeyboardButton('Курган')
    item6 = types.KeyboardButton('Нижний Тагил')
    markup.add(item1,item2)
    markup.add(item3,item4)
    markup.add(item5, item6)
    bot.send_message(message.chat.id, 'Выбери город в котором хочешь узнать погоду.\nЕсли город отсутствует, введи название на английском языке.',reply_markup=markup)

list_city={'Екатеринбург':'Ekaterinburg',
           'Челябинск':'Chelyabinsk',
           'Пермь':'Perm',
           'Тюмень':'Tyumen',
           'Нижний Тагил':'Nizhny Tagil',}
@bot.message_handler(content_types=["text"])
def hendle_text(message):
    global list_city, get_weather
    if message in list_city:
        bot.send_message(message.chat.id, get_weather(list_city[message.text]))
    else:
        bot.send_message(message.chat.id, get_weather(message.text))

bot.polling(none_stop=True, interval=0)