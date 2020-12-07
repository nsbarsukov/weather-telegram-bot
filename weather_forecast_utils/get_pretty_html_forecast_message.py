from datetime import datetime
from constants import DATE_FORMAT
from weather_forecast_utils.custom_typings import ForecastType


def get_pretty_html_forecast_message(location: str, date: datetime, forecast: ForecastType) -> str:
    main_info = forecast["main"]

    mean_temperature = main_info["temp"]
    min_temperature = main_info["temp_min"]
    max_temperature = main_info["temp_max"]
    feels_like = main_info["feels_like"]
    humidity = main_info["humidity"]

    return \
        f"""
<u><b>Прогноз погоды</b></u>
<i>{location}</i> | <i>{date.strftime(DATE_FORMAT)}</i>\n
–––––––––––––––––––––
<b>Средняя температура</b> {mean_temperature} °C
<b>Мин. температура:</b> {min_temperature} °C
<b>Макс. температура:</b> {max_temperature} °C
<b>Ощущается как:</b> {feels_like} °C
<b>Влажность:</b> {humidity} %
–––––––––––––––––––––\n
<b>Данные:</b> <a href="https://openweathermap.org/forecast5">Open Weather API</a>
<b>Автор бота:</b> <a href="https://t.me/nsbarsukov">@nsbarsukov</a>
        """