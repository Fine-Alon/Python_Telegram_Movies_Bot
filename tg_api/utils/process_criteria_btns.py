from telebot import TeleBot
from telebot.types import Message
from tg_api.utils.keyboard_criteria_search import keyboard_criteria_search as s_keys
from tg_api.utils.search_film_creteria_fncs import by_film_name, by_film_rating, by_low_budget, by_high_budget


def process_criteria_btns(bot: TeleBot, message: Message) -> None:
    """
   Обрабатывает нажатия на кнопки и устанавливает соответствующий шаг.
   :param bot: Телеграм-бот.
   :param message: Сообщение от пользователя.
   :return: None
   """
    if message.text == s_keys[0][1]:
        bot.send_message(message.chat.id,
                         'вы выбрали поиск по: {}\n\nPlease write the name of a film'.format(s_keys[0][0]))
        bot.register_next_step_handler(message, by_film_name)
    elif message.text == s_keys[1][1]:
        bot.send_message(message.chat.id,
                         'вы выбрали поиск по: {}\n\nPlease write the rating of a film'
                         '\n\nпример: 7 или 10 или 7.2-10'.format(s_keys[1][0]))
        bot.register_next_step_handler(message, by_film_rating)
    elif message.text == s_keys[2][1]:
        print(message.text)
        print(s_keys[2][1])
        bot.send_message(message.chat.id,
                         'вы выбрали: {}\n\nPlease wait a little...\n\nPlease write count of'
                         ' films you want to see\n\nпример: (1) или (4)...'.format(s_keys[2][0]))
        bot.register_next_step_handler(message, by_low_budget)
    else:
        bot.send_message(message.chat.id,
                         'вы выбрали: {}\n\nPlease wait a little...\n\nPlease write count of'
                         ' films you want to see\n\nпример: (1) или (4)...'.format(s_keys[3][0]))
        bot.register_next_step_handler(message, by_high_budget)
