from telebot import TeleBot
from telebot.types import Message
from tg_api.states.find_film import FindFilmState
from tg_api.utils.keyboard_criteria_search import keyboard_criteria_search as search_keys


def process_criteria_btns(bot: TeleBot, message: Message) -> None:
    """

    :param bot:
    :param message:
    :return: None
    """

    if message.text == search_keys[0][1]:
        bot.set_state(message.from_user.id, FindFilmState.name, message.chat.id)
        bot.send_message(message.chat.id, 'вы выбраи поиск по {}'.format(search_keys[0][0]))
    elif message.text == search_keys[1][1]:
        bot.set_state(message.from_user.id, FindFilmState.name, message.chat.id)
        bot.send_message(message.chat.id, 'вы выбраи поиск по {}'.format(search_keys[1][0]))
    elif message.text == search_keys[2][1]:
        bot.set_state(message.from_user.id, FindFilmState.name, message.chat.id)
        bot.send_message(message.chat.id, 'вы выбраи поиск по {}'.format(search_keys[2][0]))
    else:
        bot.set_state(message.from_user.id, FindFilmState.name, message.chat.id)
        bot.send_message(message.chat.id, 'вы выбраи поиск по {}'.format(search_keys[3][0]))
