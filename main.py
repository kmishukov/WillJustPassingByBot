import re
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

PAVEL_NAMES = [
    "павел", "павла", "павлу", "павлом", "павле", "павлик", "павлики", "павлика", "павлику", "павликом", "павлике",
    "паша", "паше", "пашу", "паши", "пашей", "пашки", "пашке", "пашку", "пашкой", "пашенька", "пашеньки", "пашеньке", "пашеньку", "пашенькой",
    "пашечка", "пашечки", "пашечке", "пашечку", "пашечкой", "павлуша", "павлуши", "павлуше", "павлушу", "павлушей",
    "павлушка", "павлушки", "павлушке", "павлушку", "павлушкой", "павлушенька", "павлушеньки", "павлушеньке", "павлушеньку", "павлушенькой",
    "пашка", "пашки", "пашке", "пашку", "пашкой", "пашечка", "пашечки", "пашечке", "пашечку", "пашечкой",
    "паштет", "паштета", "паштету", "паштетом", "паштете", "паштеты", "паштетов", "паштетам", "паштетами", "паштетах",
    "pavel", "pavla", "pavlu", "pavlom", "pavle", "pavlik", "pavlika", "pavliku", "pavlikom", "pavlike",
    "pasha", "pashki", "pashke", "pashku", "pashkoy", "pashen’ka", "pashen’ki", "pashen’ke", "pashen’ku", "pashen’koy",
    "pavlushka", "pavlushki", "pavlushke", "pavlushku", "pavlushkoy"
]

PAVEL_REGEX = re.compile(r"\b(" + "|".join(PAVEL_NAMES) + r")\b", re.IGNORECASE)

def handle_message(update: Update, context: CallbackContext) -> None:
    if update.message and PAVEL_REGEX.search(update.message.text):
        update.message.reply_text("Сосал?")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()