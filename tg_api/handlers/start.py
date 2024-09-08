from telebot import ContinueHandling, TeleBot
from tg_api.keyboards.reply.history_search import gen_markup_menu


def send_welcome(bot: TeleBot, message) -> ContinueHandling:
    bot.send_message(message.chat.id, 'Welcome to Movie Bot!\n\n'
                                      '\tI\'ll help you get info about films\n\n'
                                      'What can I do you for?',
                     reply_markup=gen_markup_menu())
    return ContinueHandling()
