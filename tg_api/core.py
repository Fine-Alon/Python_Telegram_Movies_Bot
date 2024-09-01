# Инициализация бота. Подключение всех необходимых модулей и запуск бота

# from config_data import config
import telebot
from telebot import ContinueHandling, StateMemoryStorage
from tg_api.utils.set_bot_commands import set_default_commands
from config_data import config

storage = StateMemoryStorage()
bot = telebot.TeleBot(config.BOT_TOKEN, state_storage=storage)

set_default_commands(bot)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, 'welcome to movie bot!'
                          ' I\'ll help you get info about films')
    return ContinueHandling()


# 2 кнопки на выбор если нужно просмотреть историб или найти фильм



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(commands=['start'])
def send_explanation(message):
    bot.send_message(message.chat.id, 'write and send name of film you want to watch')

# Код означает, что любое сообщение будет обработано с помощью
# обработчика сообщений echo_all. Его важно объявить после всех других обработчиков.
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text + '?  :)')
    bot.send_message(message.chat.id, 'Новое сообщение!')


if __name__ == "__main__":
    bot.infinity_polling()
