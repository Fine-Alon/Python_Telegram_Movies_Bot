from telebot.types import Message
from telebot import TeleBot
from loader import bot
from tg_api.states.find_film import FindFilmState


@bot.message_handler(commands=['find_film'])
def find_movie(bot: TeleBot, message: Message) -> None:
    bot.set_state(message.from_user.id, FindFilmState.film, message.chat.id)
    bot.send_message(message.from_user.id, 'Hi {}'
                                           'Please write the name of the film'.format(message.from_user.username))


@bot.message_handler(state=FindFilmState.film)
def get_film_name(message: Message) -> None:
    print('message.chat.id: ', message.chat.id)
    print('message.from_user.id: ', message.from_user.id)
    bot.send_message(message.chat.id, 'well, I\'ve got it\nPlease write the genre of the film')
    bot.set_state(message.from_user.id, FindFilmState.genre, message.chat.id)

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['film'] = message.text


@bot.message_handler(state=FindFilmState.genre)
def get_film_genre(message: Message) -> None:
    if message.text.isalpha():
        bot.send_message(message.chat.id, 'well done! I\'ve got it'
                                          'Please wait until I find films for you')
        #         here site Api fnc
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['genre'] = message.text
    else:
        bot.send_message(message.chat.id, 'Genre must be letters only!')
