from emoji import emojize

BOT_MESSAGES = {
    'start_command': emojize(
        "Привет!\nЯ чат-бот погоды:sunny::snowflake::cloud::umbrella:\nПросто напиши мне, в каком городе тебя интересует погода и на какой день.",
        use_aliases=True
    ),
    'say_bye': emojize(
        'До скорых встреч :wave:',
        use_aliases=True
    )
}