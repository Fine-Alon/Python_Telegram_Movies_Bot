from loader import bot
from telebot.types import Message, ReplyKeyboardRemove
from tg_api.utils.process_criteria_btns import process_criteria_btns


def handle_search_btns(message: Message) -> None:
    process_criteria_btns(bot, message)


# условие для выхода в главное меню
# if message.text == 'menu' or message.text == '/menu':
#     show_main_menu(bot, message)
#     return
