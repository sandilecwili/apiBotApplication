from telegram import *
from telegram.ext import *

bot = Bot("5428926600:AAF3oh_jpyO9VSdncq6A7WHPma4ng6PDL80")

updater = Updater("5428926600:AAF3oh_jpyO9VSdncq6A7WHPma4ng6PDL80", use_context=True)

dispatcher = updater.dispatcher


def test_function(update: Update, context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Have you ever tried to catch a fog? I tried yesterday but I mist.",
    )


start_value = CommandHandler('Hello', test_function)

dispatcher.add_handler(start_value)

updater.start_polling()
