from loader import bot
from telebot.types import Message, ReplyKeyboardRemove
from tg_api.states.find_film import FindFilmState
from tg_api.utils.keyboard_criteria_search import keyboard_criteria_search as s_keys


# search_keys = ['By NAME 🏷️', 'By RATING 📊', 'LOW BUDGET movie 🪫', 'HIGH BUDGET movie 🔋']
# @bot.message_handler(func=lambda message: message.text in [s_keys[0][1], s_keys[1][1], s_keys[2][1], s_keys[3][1]])
def handle_search_btns(message: Message) -> None:
    # process_criteria_btns(bot, message)
    # bot.set_state(message.from_user.id, FindFilmState.name)
    print('1', message.text)
    print('2', s_keys[0][1])
    if message.text == s_keys[0][1]:
        bot.send_message(message.chat.id,
                         'вы выбраи поиск по: {}\n\nPlease write the name of a film'.format(s_keys[0][0]))
        bot.register_next_step_handler(message, get_film_name)
    elif message.text == s_keys[1][1]:
        # bot.set_state(message.from_user.id, FindFilmState.rating, message.chat.id)
        bot.send_message(message.chat.id, 'вы выбраи поиск по {}'.format(s_keys[1][0]))
    elif message.text == s_keys[2][1]:
        # bot.set_state(message.from_user.id, FindFilmState.low_budget, message.chat.id)
        bot.send_message(message.chat.id, 'вы выбраи поиск по {}'.format(s_keys[2][0]))
    # else:
    #     bot.set_state(message.from_user.id, FindFilmState.high_budget, message.chat.id)
    #     bot.send_message(message.chat.id, 'вы выбраи поиск по {}'.format(s_keys[3][0]))

    print('1 - state: ', bot.get_state(message.from_user.id, message.chat.id))


# @bot.message_handler(func=lambda message:message.text == s_keys[0][1])
def get_film_name(message: Message):
    bot.send_message(message.chat.id, 'Well, I\'ve got it!',
                     reply_markup=ReplyKeyboardRemove())

    bot.send_message(message.chat.id, '\nWait a little!...')

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
