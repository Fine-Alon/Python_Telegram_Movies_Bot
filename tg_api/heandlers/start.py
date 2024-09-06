from telebot import ContinueHandling, TeleBot
from tg_api.keyboards.reply.history_search import gen_markup_history_search


def send_welcome(bot: TeleBot, message) -> ContinueHandling:
    bot.send_message(message.chat.id, 'welcome to movie bot!'
                                      'what can I do you for?'
                                      ' I\'ll help you get info about films',
                     reply_markup=gen_markup_history_search())
    return ContinueHandling()
