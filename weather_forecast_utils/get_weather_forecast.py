import requests
from typing import List
from weather_forecast_utils import get_city_coords
from constants import OPEN_WEATHER_API_TOKEN

from weather_forecast_utils.custom_typings import ForecastType

# forecast for 5 days with data every 3 hours by geographic coordinates
OPEN_WEATHER_URL = 'https://api.openweathermap.org/data/2.5/forecast'


def get_weather_forecast(city_name: str, date: str) -> List[ForecastType]:
    coords = get_city_coords(city_name)
    print(city_name, date, coords)

    query_params = {
        'lat': coords['latitude'],
        'lon': coords['longitude'],
        'appid': OPEN_WEATHER_API_TOKEN,
        'lang': 'ru',
        'units': 'metric'  # For temperature in Celsius
    }

    r = requests.get(url=OPEN_WEATHER_URL, params=query_params)

    return r.json()['list']
