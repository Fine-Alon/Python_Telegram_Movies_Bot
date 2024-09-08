# Инициализация бота. Подключение всех необходимых модулей и запуск бота

from loader import bot
from telebot.types import Message, ReplyKeyboardRemove
from tg_api.handlers.find_film import find_movie
from tg_api.handlers.menu import show_main_menu
from tg_api.handlers.start import send_welcome


# @bot.message_handler(commands=['menu'])
@bot.message_handler(state='*', func=lambda message: message.text.lower() == 'menu')
@bot.message_handler(func=lambda message: message.text.lower() == 'menu' or message.text.lower() == '/menu')
def handle_back_to_menu(message: Message) -> None:
    """
    Обрабатывает команды и текстовые сообщения с запросом 'menu 📋' и '/menu'.
    """

    bot.delete_state(message.from_user.id, message.chat.id)
    show_main_menu(bot, message)


@bot.message_handler(commands=['help', 'start'])
def handle_start(message: Message) -> None:
    print("handle_start сработал")  # Лог для проверки
    send_welcome(bot, message)


# может в хендлерах что то прописать??


@bot.message_handler(func=lambda message: message.text == 'history 📑')
# @bot.message_handler(commands=['history'])
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
