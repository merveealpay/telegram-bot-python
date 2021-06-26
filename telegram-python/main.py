from decouple import config
from telegram.ext import *
import responses as R

API_KEY = config('API_KEY')

print("bot started...")


def start_command(update, context):
    update.message.reply_text('Baslamak icin, random bir seyler yazabilirsin!')


def help_command(update, context):
    update.message.reply_text('Yardima ihtiyacin varsa google bakabilirsin!')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("start", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
