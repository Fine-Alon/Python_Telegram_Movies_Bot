# Инициализация бота. Подключение всех необходимых модулей и запуск бота
# callback_query_handler для inlyne button

from loader import bot
from telebot.types import Message, ReplyKeyboardRemove
from tg_api.handlers.find_film import find_movie
from tg_api.handlers.start import send_welcome

print("core.py инициализирован")


@bot.message_handler(commands=['help', 'start'])
def handle_start(message) -> None:
    print("handle_start сработал")  # Лог для проверки
    send_welcome(bot, message)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])

@bot.message_handler(func=lambda message: message.text == 'history 📑')
# @bot.message_handler(commands=['history 📑'])
def handle_history(message: Message) -> None:
    print("handle_history сработал")  # Лог для проверки
    bot.send_message(message.chat.id,
                     'запрос на данные и вывод',
                     reply_markup=ReplyKeyboardRemove())


@bot.message_handler(func=lambda message: message.text == 'search 🔎')
def handle_search(message: Message) -> None:
    print("handle_search сработал")  # Лог для проверки
    # вызов сценария по пооиску фильма
    find_movie(bot, message)
    bot.send_message(message.chat.id,
                     'сценарий поиска...',
                     reply_markup=ReplyKeyboardRemove())
