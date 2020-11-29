from emoji import emojize

DATE_FORMAT = '%d.%m.%Y'

BOT_MESSAGES = {
    'start_command': emojize(
        "Привет!\nЯ чат-бот погоды:sunny::snowflake::cloud::umbrella:\nПросто напиши мне, в каком городе тебя интересует погода и на какой день.",
        use_aliases=True
    ),
    'say_bye': emojize(
        'До скорых встреч :wave:',
        use_aliases=True
    ),
    'say_understand_nothing': emojize(
        'К сожалению, я не понял, чего вы хотите :cry:.\nДавайте попробуем всё заново?\nПросто напиши мне, в каком городе тебя интересует погода и на какой день.',
        use_aliases=True
    )
}