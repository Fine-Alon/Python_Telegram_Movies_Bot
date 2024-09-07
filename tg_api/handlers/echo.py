from telebot import TeleBot


# Код означает, что любое сообщение будет обработано с помощью
# обработчика сообщений echo_all. Его важно объявить после всех других обработчиков.
# @bot.message_handler(func=lambda message: True)
def echo_all(bot: TeleBot, message) -> None:
    bot.reply_to(message, message.text + '?  :)')
    bot.send_message(message.chat.id, 'Новое сообщение!')
