from telebot import TeleBot
from telebot.types import Message, KeyboardButton, ReplyKeyboardMarkup
from tg_api.utils.keyboard_criteria_search import keyboard_criteria_search


def search_criteria(bot: TeleBot, message: Message) -> ReplyKeyboardMarkup:
    #  📉📈
    """
    Кнопки для выбора критериа по которому искать фильм

    :param bot:
    :param message:
    :return: ReplyKeyboardMarkup
    """
    keyboard = ReplyKeyboardMarkup()
    by_name_btn = KeyboardButton(keyboard_criteria_search[0][1])
    by_rating_btn = KeyboardButton(keyboard_criteria_search[1][1])
    by_low_budget_btn = KeyboardButton(keyboard_criteria_search[2][1])
    by_high_budget_btn = KeyboardButton(keyboard_criteria_search[3][1])

    keyboard.row(by_name_btn, by_rating_btn)
    keyboard.row(by_low_budget_btn, by_high_budget_btn)

    return keyboard
