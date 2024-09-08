from telebot.types import KeyboardButton, ReplyKeyboardMarkup


def gen_markup_menu():
    # 📜📋🗂️
    history_btn = KeyboardButton(text='history 📑')
    search_btn = KeyboardButton(text='search 🔎')
    help_btn = KeyboardButton(text='help 🙋🏻‍')
    menu_btn = KeyboardButton(text='menu 📋')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(history_btn, search_btn)
    keyboard.row(help_btn, menu_btn)

    return keyboard
