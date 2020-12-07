import os

BOT_TOKEN = os.environ.get('WEATHER_BOT_TOKEN')
YANDEX_GEOCODER_API_TOKEN = os.environ.get('YANDEX_GEOCODER_API_TOKEN')
OPEN_WEATHER_API_TOKEN = os.environ.get('OPEN_WEATHER_API_TOKEN')


def check_all_tokens_set():
    """Проверка на то, что установлены все переменные глобального окружения, необходимые для работы бота"""
    return BOT_TOKEN is not None and YANDEX_GEOCODER_API_TOKEN is not None and OPEN_WEATHER_API_TOKEN is not None
