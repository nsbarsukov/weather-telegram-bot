from datetime import date
from constants import DATE_FORMAT
from weather_forecast_utils.custom_typings import ForecastType


def get_pretty_html_forecast_message(location: str, forecast_date: date, forecast: ForecastType) -> str:
    main_info = forecast["main"]
    temperature = main_info["temp"]
    feels_like = main_info["feels_like"]
    humidity = main_info["humidity"]

    wind_speed = forecast['wind']['speed']
    rain_prop = forecast['pop']

    return \
        f"""
<u><b>Прогноз погоды</b></u>
<i>{location}</i> | <i>{forecast_date.strftime(DATE_FORMAT)}</i>\n
–––––––––––––––––––––
<b>Температура воздуха</b> {temperature} °C
<b>Ощущается как:</b> {feels_like} °C
<b>Скорость ветра:</b> {wind_speed} м/с
<b>Вероятность осадков:</b> {rain_prop}
<b>Влажность:</b> {humidity} %
–––––––––––––––––––––\n
<b>Данные:</b> <a href="https://openweathermap.org/forecast5">Open Weather API</a>
<b>Автор бота:</b> <a href="https://t.me/nsbarsukov">@nsbarsukov</a>
        """