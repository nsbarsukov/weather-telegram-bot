import re

# telegram bot packages
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext

# local packages
from bot import Bot
from constants import BOT_MESSAGES


def start_command(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=BOT_MESSAGES['start_command']
    )


def say_bye(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=BOT_MESSAGES['say_bye']
    )


def msg_with_keyboard(update: Update, context: CallbackContext):
    reply_keyboard = [['Confirm', 'Restart']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    context.bot.send_message(chat_id=update.effective_chat.id, text='Как дела?', reply_markup=markup)


BOT_TOKEN = '1412832721:AAFsug46EX33UFUFh0Zfky8l0kp6Q5WfiVs'
bot = Bot(BOT_TOKEN)
bot.add_command('start', start_command)
bot.add_msg_handler(msg_with_keyboard, regexp=re.compile(r'кнопки', re.IGNORECASE | re.DOTALL))
bot.add_msg_handler(say_bye, regexp=re.compile(r'пока', re.IGNORECASE))
bot.start_polling()
