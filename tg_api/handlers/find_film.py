from loader import bot
from telebot.types import Message
from telebot import TeleBot
from tg_api.states.find_film import FindFilmState
from website_api.core import RequestSiteApi


@bot.message_handler(commands=['find_film'])
def find_movie(bot: TeleBot, message: Message) -> None:
    bot.set_state(message.from_user.id, FindFilmState.film, message.chat.id)
    bot.send_message(message.from_user.id, 'Hi {}!!!\n'
                                           'Please write the name of the film'.format(message.from_user.username))


@bot.message_handler(state=FindFilmState.film)
def get_film_name(message: Message) -> None:
    bot.send_message(message.chat.id, 'Well, I\'ve got it!\nPlease write the genre of the film')
    bot.set_state(message.from_user.id, FindFilmState.genre, message.chat.id)

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['film'] = message.text


@bot.message_handler(state=FindFilmState.genre)
def get_film_genre(message: Message) -> None:
    if message.text.isalpha():
        bot.send_message(message.chat.id, 'Well done!\n I\'ve got it\n'
                                          'Please wait until I find films for you')
        #         here site Api fnc
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['genre'] = message.text
            film = data.get('film')
            genre = message.text

        # Создаём экземпляр класса RequestSiteApi
        api_client = RequestSiteApi()
        # возможно буду передавать словарь парамтров
        api_client.get_movie_by_name()
    else:
        bot.send_message(message.chat.id, 'Genre must be letters only!')
