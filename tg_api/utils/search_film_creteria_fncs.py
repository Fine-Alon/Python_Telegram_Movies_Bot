from telebot.types import Message, ReplyKeyboardRemove
from loader import bot
from website_api.core import RequestSiteApi
from database.utils.CRUD import create_record
from website_api.utils.format_res_to_str import format_res_to_str

# Создаём экземпляр класса RequestSiteApi
api_client = RequestSiteApi()


def by_film_name(message: Message):
    print('by_film_name')
    bot.send_message(message.chat.id, 'Well, I\'ve got it!\n\nPlease wait a little...',
                     reply_markup=ReplyKeyboardRemove())

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['film'] = message.text
    print("Фильм успешно сохранён:", message.text)

    res = api_client.get_movie_by_name(message.text)
    if res == None:
        bot.send_message(message.chat.id, 'self titled film wasn\'t found')
    else:
        print(res)
        for movie_info in res:
            # Создаем строку с данными фильма
            msg = format_res_to_str(movie_info)
            bot.send_message(message.chat.id, msg)


def by_film_rating(message: Message):
    print("by_film_rating")
    bot.send_message(message.chat.id, 'Well, I\'ve got it!\n\nPlease wait a little...',
                     reply_markup=ReplyKeyboardRemove())

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['rating'] = message.text
    print("Фильм успешно сохранён:", message.text)

    # передаем параметр рейтинг
    res = api_client.get_movie_by_rating(message.text)
    for movie_info in res:
        msg = format_res_to_str(movie_info)
        bot.send_message(message.chat.id, msg)


def by_low_budget(message: Message):
    print("by_low_budget")

    bot.send_message(message.chat.id, 'Well, I\'ve got it!\n\nPlease wait a little...',
                     reply_markup=ReplyKeyboardRemove())

    res = api_client.get_movie_by_low_budget(message.text)
    for movie_info in res:
        msg = format_res_to_str(movie_info)
        bot.send_message(message.chat.id, msg)


def by_high_budget(message: Message):
    print("by_high_budget")

    bot.send_message(message.chat.id, 'Well, I\'ve got it!\n\nPlease wait a little...',
                     reply_markup=ReplyKeyboardRemove())

    res = api_client.get_movie_by_high_budget(message.text)
    for movie_info in res:
        print('movie_info: ', movie_info)
        msg = format_res_to_str(movie_info)
        bot.send_message(message.chat.id, msg)
