from telebot.types import Message, ReplyKeyboardRemove
from loader import bot
from website_api.core import RequestSiteApi

# Создаём экземпляр класса RequestSiteApi
api_client = RequestSiteApi()


def by_film_name(message: Message):
    bot.send_message(message.chat.id, 'Well, I\'ve got it!',
                     reply_markup=ReplyKeyboardRemove())
    if message.text.isalpha():
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['film'] = message.text
        print("Фильм успешно сохранён:", message.text)

        # возможно буду передавать словарь парамтров
        api_client.get_movie_by_name()
    else:
        bot.send_message(message.chat.id, 'Genre must be letters only!')
        return

    bot.send_message(message.chat.id, '\nWait a little...')


def by_film_rating(message: Message):
    bot.send_message(message.chat.id, 'Well, I\'ve got it!',
                     reply_markup=ReplyKeyboardRemove())
    if message.text.isalpha():
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['film'] = message.text
        print("Фильм успешно сохранён:", message.text)

        # возможно буду передавать словарь парамтров
        api_client.get_movie_by_name()
    else:
        bot.send_message(message.chat.id, 'Genre must be letters only!')

    bot.send_message(message.chat.id, '\nWait a little !...')


def by_low_budget(message: Message):
    bot.send_message(message.chat.id, 'Well, I\'ve got it!',
                     reply_markup=ReplyKeyboardRemove())


def by_high_budget(message: Message):
    bot.send_message(message.chat.id, 'Well, I\'ve got it!',
                     reply_markup=ReplyKeyboardRemove())
