from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def yes_or_no_markup():
    button_1 = InlineKeyboardButton(text="Yes 👍🏼", callback_data="yes")
    button_2 = InlineKeyboardButton(text="No 🙅🏻", callback_data="no")

    keyboard = InlineKeyboardMarkup()
    keyboard.add(button_1, button_2)
    return keyboard
