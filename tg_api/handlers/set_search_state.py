from telebot import TeleBot
from telebot.types import Message
from tg_api.utils.process_criteria_btns import process_criteria_btns


# search_keys = ['By NAME 🏷️', 'By RATING 📊', 'LOW BUDGET movie 🪫', 'HIGH BUDGET movie 🔋']
# @bot.message_handler(func=lambda message: message.text in [s_keys[0][1], s_keys[1][1], s_keys[2][1], s_keys[3][1]])
def handle_search_btns(bot: TeleBot, message: Message) -> None:
    process_criteria_btns(bot, message)
    print('1. State - ', bot.get_state(message.from_user.id, message.chat.id))
