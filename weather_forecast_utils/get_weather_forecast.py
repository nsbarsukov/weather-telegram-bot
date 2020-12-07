import requests
from datetime import datetime, timedelta
from weather_forecast_utils import get_city_coords
from constants import OPEN_WEATHER_API_TOKEN

from weather_forecast_utils.custom_typings import ForecastType

# forecast for 5 days with data every 3 hours by geographic coordinates
OPEN_WEATHER_URL = 'https://api.openweathermap.org/data/2.5/forecast'


def get_weather_forecast(city_name: str, for_current_date: datetime) -> ForecastType:
    coords = get_city_coords(city_name)

    query_params = {
        'lat': coords['latitude'],
        'lon': coords['longitude'],
        'appid': OPEN_WEATHER_API_TOKEN,
        'lang': 'ru',
        'units': 'metric'  # For temperature in Celsius
    }

    r = requests.get(url=OPEN_WEATHER_URL, params=query_params)
    next_5_days_forecasts = r.json()['list']

    def is_current_day_forecast(forecast: ForecastType) -> bool:
        forecast_date_unix = int(forecast['dt'])

        return for_current_date.timestamp() <= forecast_date_unix < (for_current_date + timedelta(days=1)).timestamp()

    current_date_forecasts = list(filter(lambda f: is_current_day_forecast(f), next_5_days_forecasts))

    return current_date_forecasts[int(len(current_date_forecasts) / 2)]

