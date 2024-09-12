from loader import bot
from telebot.types import Message, ReplyKeyboardRemove
from tg_api.states.find_film import FindFilmState
from tg_api.utils.keyboard_criteria_search import keyboard_criteria_search as s_keys


# search_keys = ['By NAME 🏷️', 'By RATING 📊', 'LOW BUDGET movie 🪫', 'HIGH BUDGET movie 🔋']
# @bot.message_handler(func=lambda message: message.text in [s_keys[0][1], s_keys[1][1], s_keys[2][1], s_keys[3][1]])
def handle_search_btns(message: Message) -> None:
    # process_criteria_btns(bot, message)
    print('1', message.text)

    if message.text == s_keys[0][1]:
        bot.send_message(message.chat.id,
                         'вы выбрали поиск по: {}\n\nPlease write the name of a film'.format(s_keys[0][0]))
        bot.register_next_step_handler(message, by_film_name)
    elif message.text == s_keys[1][1]:
        bot.send_message(message.chat.id,
                         'вы выбрали поиск по: {}\n\nPlease write the rating of a film'.format(s_keys[1][0]))
        bot.register_next_step_handler(message, by_film_rating)
    elif message.text == s_keys[2][1]:
        bot.send_message(message.chat.id,
                         'вы выбрали: {}\n\nPlease wait a little...'.format(s_keys[2][0]))
        bot.register_next_step_handler(message, by_low_budget)
    else:
        bot.send_message(message.chat.id,
                         'вы выбрали: {}\n\nPlease wait a little...'.format(s_keys[3][0]))
        bot.register_next_step_handler(message, by_high_budget)


def by_film_name(message: Message):
    bot.send_message(message.chat.id, 'Well, I\'ve got it!',
                     reply_markup=ReplyKeyboardRemove())

    bot.send_message(message.chat.id, '\nWait a little!...')


def by_film_rating(message: Message):
    bot.send_message(message.chat.id, 'Well, I\'ve got it!',
                     reply_markup=ReplyKeyboardRemove())

    bot.send_message(message.chat.id, '\nWait a little !...')


def by_low_budget(message: Message):
    bot.send_message(message.chat.id, 'Well, I\'ve got it!',
                     reply_markup=ReplyKeyboardRemove())


def by_high_budget(message: Message):
    bot.send_message(message.chat.id, 'Well, I\'ve got it!',
                     reply_markup=ReplyKeyboardRemove())

# условие для выхода в главное меню
# if message.text == 'menu' or message.text == '/menu':
#     show_main_menu(bot, message)
#     return


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
