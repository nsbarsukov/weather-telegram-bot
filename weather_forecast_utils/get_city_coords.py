import requests
from constants import YANDEX_GEOCODER_API_TOKEN

# взято отсюда https://yandex.ru/dev/maps/geocoder/doc/desc/concepts/input_params.html
GEO_CODE_URL = 'https://geocode-maps.yandex.ru/1.x'


def get_city_coords(cityName: str):
    # дополнительные query параметры смотри здесь
    # https://yandex.ru/dev/maps/geocoder/doc/desc/concepts/input_params.html
    query_params = {'apikey': YANDEX_GEOCODER_API_TOKEN, 'geocode': cityName, 'format': 'json'}
    r = requests.get(url=GEO_CODE_URL, params=query_params)

    response = r.json()['response']
    point = response['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')

    return {
        # долгота
        "longitude": point[0],
        # широта
        "latitude": point[1],
    }
