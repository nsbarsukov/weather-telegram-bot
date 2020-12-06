# weather-telegram-bot
Телеграмм-бот, рассказывающий о погоде.
Написан на python. Применяются техники nlp.

## Что осталось доделать
- [x] Сделать основной фундамент бота: базовые команды и флоу с выбором города и даты
- [x] Сделать извлечение городов и дат из текста пользователя с помощью библиотеки natasha
- [ ] Подтянуть api какого-нибудь сервиса с прознозом погоды
(создать папку weather-api-parser с утилитой `getWeatherForecast(city, date)`) 
- [ ] Заиспользовать утилиту `getWeatherForecast(city, date)` внутри `show_weather_forecast`
и сделать красивый вывод информации для пользователя
- [] Сохранить токен бота как глобальную переменную окружения и выпилить его с гита
 

## Используемые библиотеки
Перед запуском проекта необходимо установить следующие пакеты:
- **python-telegram-bot** - библиотека-обертка для работы с api телеграмма ([подробнее здесь](#почему-выбрана-python-telegram-bot-библиотека))
- **natasha** - библиотека для nlp при работе с русским текстом ([подробнее здесь](https://habr.com/ru/post/516098/))
- **emoji** - пригодится для работы со смайликами

Используй команду `pip3 install python-telegram-bot natasha emoji`

## Запуск бота
- В файле constants/global_env_variables.py в константе BOT_TOKEN подставь токен своего бота
(как создать бота и получить токен [можно почитать здесь](https://vc.ru/dev/156853-telegram-bot-dlya-polucheniya-adresa-po-lokacii-ili-koordinatam-python))
- Запусти скрипт в корне репозитория `weather_bot.py`

## Цель:
- написать чат бота, который будет говорить погоду в двух городах - Москва и СПб
- Бот должен уметь здороваться, прощаться.
- Попрощаться - значит закончить беседу.
- Бот должен как-то реагировать на непонятные высказывания
- Базу погоды составить самим - на два дня, на два города.
- Бот должен работать и продолжать вас что-то справшивать пока вы не закончите беседу.
- Один из сценаривает скрипта:
    1. Написать функцию распознания интенции
    2. Функция для того, чтобы здороваться
    3. Функция, чтобы прощаться.
    4. Функция для ошибок.
    5. Цикл while пока с агентом не попрощаются
    
## Полезные ссылочки с tutorial по написанию бота
- [Полное руководство Python по созданию Telegram Bot с использованием python-telegram-bot (статья от 7 мая 2020)](https://dev-gang.ru/article/ja-postroil-telegrafnyi-bot-dlja-borby-s-pisczevymi-othodami-vot-kak-eto-delaetsja-inaqfmq470/)
- [Telegram-бот для получения адреса по локации или координатам с использованием python-telegram-bot (статья от 9 сентября 2020)](https://vc.ru/dev/156853-telegram-bot-dlya-polucheniya-adresa-po-lokacii-ili-koordinatam-python)
- [Telegram-бот на python-telegram-bot + flask + heroku deploy](https://www.toptal.com/python/telegram-bot-tutorial-python)
- [Статья на TProger по созданию телеграмм чат бота и его deploy на Heroku](https://tproger.ru/translations/telegram-bot-create-and-deploy/)
- [Пакет natasha для nlp на русском языке](https://habr.com/ru/post/516098/)
- [Как отправлять смайлики через telegram bot](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Emoji)
и [emoji cheat sheet](https://www.webfx.com/tools/emoji-cheat-sheet/)


## Почему выбрана python-telegram-bot библиотека
На момент создания бота для Python имелось 2 крупных библиотеки согласно странице на официальном сайте телеграмма
в разделе ["Bot Code Examples"](https://core.telegram.org/bots/samples):
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)

Обе либы разрабатывали с 2015 (согласно статистике релизов) и активно разрабатываются до сих пор.
Выбор в пользу python-telegram-bot был сделан крайне примитивно:
с 2015 года по 2020 он собрал в 3 раза больше звезд и форков, чем его конкурент
(была цель научиться пользоваться инструментом, которое широко одобрило сообщество).