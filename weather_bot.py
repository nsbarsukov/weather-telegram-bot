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


def specify_date(update: Update, context: CallbackContext, city: str):
    reply_keyboard = [
        ['Сегодня', 'Завтра', 'Послезавтра'],
        ['11.12', '12.12', '13.12']
    ]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='На какой день Вам интересен прогноз в городе "{}"?'.format(city),
        reply_markup=markup
    )


def show_weather_forecast(update: Update, context: CallbackContext, location: str, date):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Показываю прогноз погоды для города "{} на {}"?'.format(location, date)
    )


def say_understand_nothing(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=BOT_MESSAGES['say_understand_nothing']
    )


def message_commander(update: Update, context: CallbackContext):
    """
    Точка входа для любых сообщений, не связанных с командами.
    Определяет, какую функцию бота запустить дальше (какой дать отклик)
    """
    user_text = update.message.text
    user_text_info = NatashaExtractor(update.message.text)
    locations = user_text_info.find_locations()
    dates = user_text_info.find_date()

    if len(locations) > 0 and len(dates) > 0:
        show_weather_forecast(update, context, locations[0], dates[0])
    elif len(locations) > 0 and len(dates) == 0:
        specify_date(update, context, locations[0])
    elif find_bye_messages_regexp.search(user_text):
        say_bye(update, context)
    else:
        say_understand_nothing(update, context)


BOT_TOKEN = '1412832721:AAFsug46EX33UFUFh0Zfky8l0kp6Q5WfiVs'
bot = Bot(BOT_TOKEN)
bot.add_command('start', start_command)
bot.add_msg_handler(message_commander)
bot.start_polling()
