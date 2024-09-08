from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardMarkup
from tg_api.keyboards.reply.history_search import gen_markup_history_search


def show_main_menu(bot: TeleBot, message: Message):
    """
    Функция для отображения главного меню.
    """
    print('menu.py сработал')
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('search 🔎', 'history 📑')
    markup.row('help', 'menu')

    bot.send_message(message.chat.id, "Главное меню", reply_markup=markup)

    # bot.send_message(message.chat.id, 'Main menu', reply_markup=gen_markup_history_search())
