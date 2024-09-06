from telebot.types import KeyboardButton, ReplyKeyboardMarkup


def gen_markup_history_search():
    # 📜📋🗂️
    history_btn = KeyboardButton(text='history 📑')
    search_btn = KeyboardButton(text='search 🔎')
    keyboard = ReplyKeyboardMarkup()
    keyboard.add(history_btn, search_btn)

    return keyboard
