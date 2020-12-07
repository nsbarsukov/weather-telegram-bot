from datetime import date, timedelta, datetime
from typing import List
from emoji import emojize

# telegram bot packages
from natasha.obj import Date
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext

# local packages
from bot import Bot
from natasha_utils import NatashaExtractor
from constants import BOT_TOKEN, BOT_MESSAGES, DATE_FORMAT, find_bye_messages_regexp
from weather_forecast_utils import get_weather_forecast


def date_after_today(n, data_format=DATE_FORMAT):
    today = date.today()

    return (today + timedelta(days=n)).strftime(data_format)


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


def say_understand_nothing(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=BOT_MESSAGES['say_understand_nothing']
    )


def specify_date(update: Update, context: CallbackContext, locations: List[str]):
    reply_keyboard = [
        [
            'Сегодня\n({})'.format(date_after_today(0)),
            'Завтра\n({})'.format(date_after_today(1)),
            'Послезавтра\n({})'.format(date_after_today(2))
         ],
        [date_after_today(3), date_after_today(4), date_after_today(5)]
    ]

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='На какой день Вам интересен прогноз в городе "{}"?'.format(locations[0]),
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )


def show_weather_forecast(update: Update, context: CallbackContext, locations: List[str], dates: List[Date]):
    day = dates[0]
    parsed_date = datetime(day.year or date.today().year, day.month, day.day)

    forecast = get_weather_forecast(locations[0], parsed_date)
    print(forecast)

    # TODO Подтянуть api какого-нибудь сервиса с прознозом погоды
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Показываю прогноз погоды для города "{}" на {}?'.format(locations[0], parsed_date.strftime(DATE_FORMAT))
    )


def message_commander(update: Update, context: CallbackContext, bot_ref: Bot):
    """
    Точка входа для любых сообщений, не связанных с командами.
    Определяет, какую функцию бота запустить дальше (какой дать отклик)
    """
    bot_storage_state = bot_ref.get_storage_state()
    remembered_locations = bot_storage_state['locations'] if 'locations' in bot_storage_state else None

    user_text = update.message.text
    user_text_info = NatashaExtractor(update.message.text)
    locations = user_text_info.find_locations() or remembered_locations or []
    dates = user_text_info.find_date()

    if len(locations) > 0 and len(dates) > 0:
        show_weather_forecast(update, context, locations, dates)
        bot_ref.reset_storage()
    elif len(locations) > 0 and len(dates) == 0:
        bot_ref.save_to_storage('locations', locations)
        specify_date(update, context, locations)
    elif find_bye_messages_regexp.search(user_text):
        say_bye(update, context)
        bot_ref.reset_storage()
    else:
        say_understand_nothing(update, context)
        bot_ref.reset_storage()


bot = Bot(BOT_TOKEN)
bot.add_command('start', start_command)
bot.add_msg_handler(lambda update, context: message_commander(update, context, bot))
bot.start_polling()
print(emojize("==============> Бот запущен :rocket: <==============", use_aliases=True))
