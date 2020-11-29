# telegram bot packages
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext

# local packages
from bot import Bot
from natasha_utils import NatashaExtractor
from constants import BOT_MESSAGES, find_bye_messages_regexp


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


def ask_if_correct_city(update: Update, context: CallbackContext, city: str):
    reply_keyboard = [['Да', 'Нет']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Вам интересен город "{}"?'.format(city),
        reply_markup=markup
    )


def message_commander(update: Update, context: CallbackContext):
    """
    Точка входа для любых сообщений, не связанных с коммандами.
    Определяет, какую функцию бота запустить дальше (какой дать отклик)
    """
    user_text = update.message.text
    user_text_info = NatashaExtractor(user_text)
    locations = user_text_info.find_locations()

    if find_bye_messages_regexp.search(user_text):
        say_bye(update, context)
    elif len(locations) > 0:
        ask_if_correct_city(update, context, locations[0])


BOT_TOKEN = '1412832721:AAFsug46EX33UFUFh0Zfky8l0kp6Q5WfiVs'
bot = Bot(BOT_TOKEN)
bot.add_command('start', start_command)
bot.add_msg_handler(message_commander)
bot.start_polling()
