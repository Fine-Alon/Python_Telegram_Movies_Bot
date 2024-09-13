from loader import bot
from telebot.types import Message, ReplyKeyboardRemove
from tg_api.handlers.find_film import handle_search_btns
from tg_api.handlers.menu import show_main_menu
from tg_api.handlers.start import send_welcome
from tg_api.keyboards.reply.search_criteria import search_criteria
from tg_api.utils.keyboard_criteria_search import keyboard_criteria_search as s_keys


@bot.message_handler(commands=['help', 'start'])
def handle_start(message: Message) -> None:
    send_welcome(bot, message)


@bot.message_handler(state='*', func=lambda message: message.text.lower() == 'menu')
@bot.message_handler(func=lambda message: message.text.lower() == 'menu' or message.text.lower() == '/menu')
def handle_back_to_menu(message: Message) -> None:
    """
    Обрабатывает команды и текстовые сообщения с запросом 'menu 📋' и '/menu'.
    """

    bot.delete_state(message.from_user.id, message.chat.id)
    show_main_menu(bot, message)


@bot.message_handler(func=lambda message: message.text == 'history 📑')
# @bot.message_handler(commands=['history'])
def handle_history(message: Message) -> None:
    print("handle_history сработал")  # Лог для проверки
    bot.send_message(message.chat.id,
                     'запрос на данные и вывод',
                     reply_markup=ReplyKeyboardRemove())


@bot.message_handler(func=lambda message: message.text == 'search 🔎')
def handle_search(message: Message) -> None:
    bot.send_message(message.from_user.id, 'Hi {}!!!\n\n'
                                           'please choice the movie criteria you would like to search by'.format(
        message.from_user.username),
                     reply_markup=search_criteria(bot, message))

# s_keys/search_keys = ['By NAME 🏷️', 'By RATING 📊', 'LOW BUDGET movie 🪫', 'HIGH BUDGET movie 🔋']
@bot.message_handler(func=lambda message: message.text in [s_keys[0][1],
                                                           s_keys[1][1],
                                                           s_keys[2][1],
                                                           s_keys[3][1]])
# вызов сценария по пооиску фильма
def handle_search(message):
    handle_search_btns(message)
