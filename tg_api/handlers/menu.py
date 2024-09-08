from telebot import TeleBot
from telebot.types import Message
from tg_api.keyboards.reply.history_search import gen_markup_menu


def show_main_menu(bot: TeleBot, message: Message):
    """
    Функция для отображения главного меню.
    """
    print('menu.py сработал')
    bot.send_message(message.chat.id, "Main menu", reply_markup=gen_markup_menu())
