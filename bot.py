import telebot
import os
import api
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

if not bot_token:
    raise ValueError("TELEGRAM_BOT_TOKEN is missing. Please check your .env file.")

def run():
    bot = telebot.TeleBot(bot_token)

    @bot.message_handler(commands=["start"])
    def handle_start(message):
        """
        handler for start command
        """
        bot.send_message(message.chat.id, "Hello! \n Send Me desired currency symbol to see price :")

    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        """
        if text message is a currency symbol and it is available in list_of_available_currencies, send price.
        """
        text = message.text.upper()
        if text in api.list_of_available_currencies():
            currency_symbol = text
            currency_price = api.get_currency_price_by_symbol(currency_symbol)
            bot.send_message(message.chat.id, currency_price)

    bot.polling()