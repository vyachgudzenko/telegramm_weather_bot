import telebot
from telebot import types
from config import token
from parsing import get_html, get_data

bot = telebot.TeleBot(token)
print("Бот Sinoptik_weather_bot запущен")
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, в каком городе ты хочешь узнать погоду? Просто напиши его название на русском')

@bot.message_handler(content_types=["text"])
def weather_msg(message):
    try:
        html = get_html(message.text)
        data = get_data(html)
        msg_for_bot = "Сегодня ожидается такая погода. Температура от" + data[0] + " до" + data[1] + "." + data[2]
        bot.send_message(message.chat.id, msg_for_bot)
    except AttributeError as e:
        bot.send_message(message.chat.id,"Что-то пошло не так... Попробуй ввести корректное название города.")

bot.polling()
