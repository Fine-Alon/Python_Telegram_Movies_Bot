from loader import bot
import tg_api
from telebot.custom_filters import StateFilter
from tg_api.utils.set_bot_commands import set_default_commands
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    try:
        print("main.py запущен")
        bot.add_custom_filter(StateFilter(bot))
        set_default_commands(bot)
        bot.infinity_polling()
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
