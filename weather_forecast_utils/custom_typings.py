from typing import TypedDict, List


class WindType(TypedDict):
    speed: float
    deg: float


class WeatherComments(TypedDict):
    description: str


class MainForecastInfo(TypedDict):
    feels_like: float
    grnd_level: int
    humidity: int
    pressure: int
    sea_level: int
    temp: float
    temp_kf: float
    temp_max: float
    temp_min: float


class ForecastType(TypedDict):
    dt: int
    dt_txt: str
    wind: WindType
    weather: List[WeatherComments]
    main: MainForecastInfo
    pop: int
