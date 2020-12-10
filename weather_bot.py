from datetime import date, timedelta, datetime
from typing import List
from emoji import emojize

# telegram bot packages
from telegram import Update, ReplyKeyboardMarkup, ParseMode
from telegram.ext import CallbackContext

# local packages
from bot import Bot
from natasha_utils import NatashaExtractor
from constants import BOT_TOKEN, BOT_MESSAGES, DATE_FORMAT, find_bye_messages_regexp, check_all_tokens_set
from weather_forecast_utils import get_weather_forecast, get_pretty_html_forecast_message


def date_after_today(n, data_format=DATE_FORMAT):
    today = date.today()

    return (today + timedelta(days=n)).strftime(data_format)


def start_command(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=BOT_MESSAGES['start_command']
    )


def reset_command(update: Update, context: CallbackContext, bot_ref: Bot):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=BOT_MESSAGES['reset_command']
    )
    bot_ref.reset_storage()


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
         ],
        [date_after_today(2), date_after_today(3), date_after_today(4)]
    ]

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='На какой день Вам интересен прогноз в городе "{}"?'.format(locations[0]),
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )


def show_weather_forecast(update: Update, context: CallbackContext, locations: List[str], dates: List[date]):
    day = dates[0]
    parsed_date = datetime(day.year or date.today().year, day.month or date.today().month, day.day or date.today().day)

    forecast = get_weather_forecast(locations[0], parsed_date)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=get_pretty_html_forecast_message(locations[0], parsed_date, forecast),
        disable_web_page_preview=True,
        parse_mode=ParseMode.HTML
    )


def message_commander(update: Update, context: CallbackContext, bot_ref: Bot):
    """
    Точка входа для любых сообщений, не связанных с командами.
    Определяет, какую функцию бота запустить дальше (какой дать отклик)
    """
    bot_storage_state = bot_ref.get_storage_state()
    remembered_locations = bot_storage_state['locations'] if 'locations' in bot_storage_state else None
    already_specify_date = bot_storage_state['already_specify_date'] if 'already_specify_date' in bot_storage_state else None

    user_text = update.message.text
    user_text_info = NatashaExtractor(update.message.text)
    locations = user_text_info.find_locations() or remembered_locations or []
    dates = user_text_info.find_date()

    if len(locations) > 0 and len(dates) > 0:
        show_weather_forecast(update, context, locations, dates)
        bot_ref.reset_storage()
    elif len(locations) > 0 and len(dates) == 0 and not already_specify_date:
        bot_ref.save_to_storage('locations', locations)
        specify_date(update, context, locations)
        bot_ref.save_to_storage('already_specify_date', True)
    elif find_bye_messages_regexp.search(user_text):
        say_bye(update, context)
        bot_ref.reset_storage()
    else:
        say_understand_nothing(update, context)
        bot_ref.reset_storage()


if check_all_tokens_set():
    bot = Bot(BOT_TOKEN)
    bot.add_command('start', start_command)
    bot.add_command('reset', lambda update, context: reset_command(update, context, bot))
    bot.add_msg_handler(lambda update, context: message_commander(update, context, bot))
    bot.start_polling()
    print(emojize("==============> Бот запущен :rocket: <==============", use_aliases=True))
else:
    print(emojize(
        ":x: Не установлены все переменные глобального окружения, необходимые для работы бота! :x:",
        use_aliases=True)
    )
    print(emojize(
        'Смотри пункт "Запуск бота" в README из корня репозитория https://github.com/nsbarsukov/weather-telegram-bot#%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D0%BA-%D0%B1%D0%BE%D1%82%D0%B0',
        use_aliases=True)
    )
