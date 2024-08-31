import telebot
from telebot import ContinueHandling

from config_data.config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, 'welcome to movie bot! I\'ll help you get info about films')
    return ContinueHandling()

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(commands=['start'])
def send_explanation(message):
    bot.send_message(message.chat.id, 'write and send name of film you want to watch')


bot.infinity_polling()
