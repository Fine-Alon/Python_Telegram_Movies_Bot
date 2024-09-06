from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def gen_markup_welcome():
    button = KeyboardButton(text='Запустить 🎬🚀')
    markup = ReplyKeyboardMarkup()
    markup.add(button)

    return markup
