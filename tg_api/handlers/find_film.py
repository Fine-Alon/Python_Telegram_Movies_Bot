from loader import bot
from telebot.types import Message
from telebot import TeleBot
from tg_api.handlers.menu import show_main_menu
from tg_api.keyboards.reply.search_criteria import search_criteria
from tg_api.states.find_film import FindFilmState
from tg_api.utils.keyboard_criteria_search import keyboard_criteria_search as s_keys
from tg_api.utils.process_criteria_btns import process_criteria_btns
from website_api.core import RequestSiteApi


@bot.message_handler(commands=['find_film'])
def find_movie(bot: TeleBot, message: Message) -> None:
    bot.send_message(message.from_user.id, 'Hi {}!!!\n\n'
                                           'please choice the movie criteria you would like to search by'.format(
        message.from_user.username),
                     reply_markup=search_criteria(bot, message))


# search_keys = 'By NAME 🏷️', 'By RATING 📊', 'LOW BUDGET movie 🪫', 'HIGH BUDGET movie 🔋']
@bot.message_handler(func=lambda message: message.text in [s_keys[0][1], s_keys[1][1], s_keys[2][1], s_keys[3][1]])
def handle_search_btns(message: Message) -> None:
    process_criteria_btns(bot, message)


@bot.message_handler(state=FindFilmState.name)
def get_film_name(message: Message) -> None:
    if message.text == 'menu' or message.text == '/menu':
        show_main_menu(bot, message)
        return

    bot.send_message(message.chat.id, 'Well, I\'ve got it!\nPlease write the genre of the film')
    bot.set_state(message.from_user.id, FindFilmState.rating, message.chat.id)

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['film'] = message.text


@bot.message_handler(state=FindFilmState.rating)
def get_film_genre(message: Message) -> None:
    if message.text == 'menu' or message.text == '/menu':
        bot.delete_state(message.from_user.id, message.chat.id)
        show_main_menu(bot, message)
        return

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
