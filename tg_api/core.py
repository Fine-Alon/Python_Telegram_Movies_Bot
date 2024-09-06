# Инициализация бота. Подключение всех необходимых модулей и запуск бота
# callback_query_handler для inlyne button

import telebot
from telebot import ContinueHandling, StateMemoryStorage
from telebot.types import Message, ReplyKeyboardRemove
from telebot.custom_filters import StateFilter

from tg_api.heandlers.start import send_welcome
from tg_api.keyboards.reply.history_search import gen_markup_history_search
from tg_api.utils.set_bot_commands import set_default_commands
from config_data import config

storage = StateMemoryStorage()
bot = telebot.TeleBot(config.BOT_TOKEN, state_storage=storage)

bot.add_custom_filter(StateFilter(bot))
set_default_commands(bot)


@bot.message_handler(commands=['help', 'start'])
def handle_start(message):
    send_welcome(bot, message)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(commands=['start'])
def send_explanation(message):
    bot.send_message(message.chat.id, 'write and send name of film you want to watch')


@bot.message_handler(func=lambda message: message.text == 'history 📑')
# @bot.message_handler(commands=['history 📑'])
def handle_history(message: Message):
    bot.send_message(message.chat.id,
                     'запрос на данные и вывод',
                     reply_markup=ReplyKeyboardRemove())


@bot.message_handler(func=lambda message: message.text == 'search 🔎')
def handle_search(message: Message):
    bot.send_message(message.chat.id,
                     'сценарий поиска...',
                     reply_markup=ReplyKeyboardRemove())


# Код означает, что любое сообщение будет обработано с помощью
# обработчика сообщений echo_all. Его важно объявить после всех других обработчиков.
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text + '?  :)')
    bot.send_message(message.chat.id, 'Новое сообщение!')


if __name__ == "__main__":
    bot.infinity_polling()
