from telebot import ContinueHandling
from tg_api.core import bot


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, 'welcome to movie bot!'
                          ' I\'ll help you get info about films')
    return ContinueHandling()
