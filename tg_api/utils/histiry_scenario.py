from loader import bot
import re
from database.utils.CRUD import get_record

date_regex = re.compile(r"\d{4}-\d{2}-\d{2}")


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == 'yes')
def history_by_date(callback_query):
    # Удаляем клавиатуру.
    bot.edit_message_reply_markup(
        callback_query.from_user.id, callback_query.message.message_id
    )
    bot.send_message(
        callback_query.from_user.id,
        "Input date in format as:     2024-09-15",
    )


@bot.message_handler(func=lambda message: date_regex.match(message.text))
def show_history_by_date(message):
    history = get_record(message.from_user.id, message.text)
    for movie in history:
        bot.send_message(message.from_user.id, movie)


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == 'no')
def show_full_history(callback_query):
    history = get_record(callback_query.from_user.id, None)
    for movie in history:
        bot.send_message(callback_query.from_user.id, movie)
