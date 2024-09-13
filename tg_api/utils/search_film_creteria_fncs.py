from telebot.types import Message, ReplyKeyboardRemove
from loader import bot
from website_api.core import RequestSiteApi

# Создаём экземпляр класса RequestSiteApi
api_client = RequestSiteApi()


def by_film_name(message: Message):
    print('by_film_name')
    bot.send_message(message.chat.id, 'Well, I\'ve got it!\n\nWait a little !...',
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
            msg = (
                f"Название: {movie_info.get('Название', 'N/A')}\n"
                f"Описание: {movie_info.get('Описание', 'N/A')}\n"
                f"Рейтинг: {movie_info.get('Рейтинг', 'N/A')}\n"
                f"Год производства: {movie_info.get('Год производства', 'N/A')}\n"
                f"Жанр: {movie_info.get('Жанр', 'N/A')}\n"
                f"Возрастной рейтинг: {movie_info.get('Возрастной рейтинг', 'N/A')}\n"
                f"Постер: {movie_info.get('Постер', 'N/A')}\n"
            )
            bot.send_message(message.chat.id, msg)


def by_film_rating(message: Message):
    print("by_film_rating")
    bot.send_message(message.chat.id, 'Well, I\'ve got it!\n\nWait a little !...',
                     reply_markup=ReplyKeyboardRemove())

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['rating'] = message.text
    print("Фильм успешно сохранён:", message.text)

    # передаем параметр рейтинг
    api_client.get_movie_by_rating(message.text)


def by_low_budget(message: Message):
    bot.send_message(message.chat.id, 'Well, I\'ve got it!',
                     reply_markup=ReplyKeyboardRemove())


def by_high_budget(message: Message):
    bot.send_message(message.chat.id, 'Well, I\'ve got it!',
                     reply_markup=ReplyKeyboardRemove())
