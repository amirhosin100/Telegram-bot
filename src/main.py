import telebot
from config.settings import TELEGRAM_TOKEN

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler()
def send_welcome(message):
	bold_message = str(message.text).upper()
	bot.reply_to(message,bold_message)

bot.infinity_polling()

