from telebot.types import Message, ReplyKeyboardRemove
from loader import bot
from website_api.core import RequestSiteApi
from website_api.utils.format_res_to_str import format_res_to_str

# Создаём экземпляр класса RequestSiteApi
api_client = RequestSiteApi()


def by_film_name(message: Message):
    print('by_film_name')
    bot.send_message(message.chat.id, 'Well, I\'ve got it!\n\nPlease wait a little...',
                     reply_markup=ReplyKeyboardRemove())

    res = api_client.get_movie_by_name(outcome_params=message.text, user_id=message.from_user.id)
    if res == None:
        bot.send_message(message.chat.id, 'self titled film wasn\'t found')
    else:
        for movie_info in res:
            # Создаем строку с данными фильма
            msg = format_res_to_str(movie_info)
            bot.send_message(message.chat.id, msg)


def by_film_rating(message: Message):
    print("by_film_rating")
    bot.send_message(message.chat.id, 'Well, I\'ve got it!\n\nPlease wait a little...',
                     reply_markup=ReplyKeyboardRemove())

    # передаем параметр рейтинг
    res = api_client.get_movie_by_rating(outcome_params=message.text, user_id=message.from_user.id)
    for movie_info in res:
        msg = format_res_to_str(movie_info)
        bot.send_message(message.chat.id, msg)


def by_low_budget(message: Message):
    print("by_low_budget")

    bot.send_message(message.chat.id, 'Well, I\'ve got it!\n\nPlease wait a little...',
                     reply_markup=ReplyKeyboardRemove())

    res = api_client.get_movie_by_low_budget(outcome_params=message.text, user_id=message.from_user.id)
    for movie_info in res:
        msg = format_res_to_str(movie_info)
        bot.send_message(message.chat.id, msg)


def by_high_budget(message: Message):
    print("by_high_budget")

    bot.send_message(message.chat.id, 'Well, I\'ve got it!\n\nPlease wait a little...',
                     reply_markup=ReplyKeyboardRemove())

    res = api_client.get_movie_by_high_budget(outcome_params=message.text, user_id=message.from_user.id)
    for movie_info in res:
        msg = format_res_to_str(movie_info)
        bot.send_message(message.chat.id, msg)
