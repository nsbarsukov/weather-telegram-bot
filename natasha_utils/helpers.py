import re
from datetime import date, datetime, timedelta
from typing import List
from natasha.obj import Date


def find_dates_as_word(text: str) -> List[date]:
    dates_as_word = []
    today = date.today()

    if re.compile(r'(сегодня)|(сейчас)', re.IGNORECASE).search(text):
        dates_as_word.append(today)

    if re.compile(r'послезавтра', re.IGNORECASE).search(text):
        dates_as_word.append(today + timedelta(days=2))
    elif re.compile(r'завтра', re.IGNORECASE).search(text):
        dates_as_word.append(today + timedelta(days=1))

    return dates_as_word


def parse_natasha_date_to_datetime(date_str: Date) -> date:
    return datetime(date_str.year or date.today().year, date_str.month or date.today().month, date_str.day or date.today().day)
