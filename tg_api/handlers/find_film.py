from telebot.states.sync.context import StateContext
from loader import bot
from telebot.types import Message, ReplyKeyboardRemove
from telebot import TeleBot
from tg_api.handlers.menu import show_main_menu
from tg_api.keyboards.reply.search_criteria import search_criteria
from tg_api.states.find_film import FindFilmState
from tg_api.utils.keyboard_criteria_search import keyboard_criteria_search as s_keys
from tg_api.utils.process_criteria_btns import process_criteria_btns


@bot.message_handler(commands=['find_film'])
def find_movie(bot: TeleBot, message: Message) -> None:
    bot.send_message(message.from_user.id, 'Hi {}!!!\n\n'
                                           'please choice the movie criteria you would like to search by'.format(
        message.from_user.username),
                     reply_markup=search_criteria(bot, message))


# search_keys = ['By NAME 🏷️', 'By RATING 📊', 'LOW BUDGET movie 🪫', 'HIGH BUDGET movie 🔋']
@bot.message_handler(func=lambda message: message.text in [s_keys[0][1], s_keys[1][1], s_keys[2][1], s_keys[3][1]])
def handle_search_btns(message: Message, state: StateContext) -> None:
    process_criteria_btns(bot, message, state)
    print('1. State - ', state.get())


@bot.message_handler(state=FindFilmState.name)
def get_film_criteria(message: Message, state: StateContext):
    bot.send_message(message.chat.id, 'Well, I\'ve got it!',
                     reply_markup=ReplyKeyboardRemove())

    if message.text == s_keys[0][1]:
        bot.send_message(message.chat.id, '\nPlease write the name of a film')

# условие для выхода в главное меню
# if message.text == 'menu' or message.text == '/menu':
#     show_main_menu(bot, message)
#     return


# if message.text == s_keys[1][1]:
#     bot.send_message(message.chat.id, '\nPlease write the rating of a film')
# if message.text == s_keys[2][1]:
#     bot.send_message(message.chat.id, '\nPlease wait a little...')
# if message.text == s_keys[3][1]:
#     bot.send_message(message.chat.id, '\nPlease wait a little...')
# bot.send_message(message.chat.id, f'{bot.get_state(message.from_user.id, message.chat.id)}')


# def aaaa(message: Message, state: StateContext):
#     state.set(FindFilmState.rating)
#     state.add_data(name=message.text)
#
# with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#     data['film'] = message.text
# print("Фильм успешно сохранён:", message.text)

# @bot.message_handler(state=FindFilmState.rating)
#         # Создаём экземпляр класса RequestSiteApi
#         api_client = RequestSiteApi()
#         # возможно буду передавать словарь парамтров
#         api_client.get_movie_by_name()
#     else:
#         bot.send_message(message.chat.id, 'Genre must be letters only!')
