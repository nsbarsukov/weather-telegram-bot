# weather-telegram-bot
Телеграмм-бот, рассказывающий о погоде.
Написан на python. Применяются техники nlp.

Для получения координат города по его названию используется
[Yandex API для перевода географических координат в адрес и наоборот](https://yandex.ru/dev/maps/geocoder/). <br>
Для получения прогноза погоды по полученным координатам используется [Open Weather API](https://openweathermap.org/forecast5).


## Что осталось доделать
- [x] Сделать основной фундамент бота: базовые команды и флоу с выбором города и даты
- [x] Сделать извлечение городов и дат из текста пользователя с помощью библиотеки natasha
- [ ] Подтянуть api какого-нибудь сервиса с прознозом погоды
(создать папку weather-api-parser с утилитой `getWeatherForecast(city, date)`) 
- [ ] Заиспользовать утилиту `getWeatherForecast(city, date)` внутри `show_weather_forecast`
и сделать красивый вывод информации для пользователя
- [x] Сохранить токен бота как глобальную переменную окружения и выпилить его с гита
 

## Используемые библиотеки
Перед запуском проекта необходимо установить следующие пакеты:
- **python-telegram-bot** - библиотека-обертка для работы с api телеграмма ([подробнее здесь](#почему-выбрана-python-telegram-bot-библиотека))
- **natasha** - библиотека для nlp при работе с русским текстом ([подробнее здесь](https://habr.com/ru/post/516098/))
- **emoji** - пригодится для работы со смайликами
- **requests** - для работы с api yandex

## Запуск бота
0. Иметь установленный python версии >= 3.8
   
1. Загрузи все используемые библиотеки командой: <br>
`pip3 install python-telegram-bot natasha emoji requests`
  
2. В файле `constants/global_env_variables.py` нужно задать токены для работы с апишками. <br> <br>
**Рекомендуемый вариант**: ничего не менять в коде, а задать каждую переменную в глобальном окружении своего компьютера (как создавать глобальные переменные окружения для bash/zsh [здесь](https://apple.stackexchange.com/a/356455)). <br>
**Легкий и быстрый вариант** (только для локального запуска!): Ты можешь просто заменить каждую переменную в духе `BOT_TOKEN = os.environ.get('BOT_TOKEN')` на `BOT_TOKEN="your token"`. <br> <br>
**Список всех констант-токенов, которые нужно задать:**
    + в константе `BOT_TOKEN` подставь токен своего бота (как создать бота и получить токен [можно почитать здесь](https://vc.ru/dev/156853-telegram-bot-dlya-polucheniya-adresa-po-lokacii-ili-koordinatam-python))
    + в константе `YANDEX_GEOCODER_API_TOKEN` подставь токен для [API для перевода географических координат в адрес и наоборот](https://yandex.ru/dev/maps/geocoder/). <br>

3. Запусти скрипт в корне репозитория `weather_bot.py`

## Цель:
- написать чат бота, который будет говорить погоду в двух городах — Москва и СПб
- Бот должен уметь здороваться, прощаться.
- Попрощаться — значит закончить беседу.
- Бот должен как-то реагировать на непонятные высказывания
- Базу погоды составить самим — на два дня, на два города.
- Бот должен работать и продолжать вас что-то спрашивать пока вы не закончите беседу.
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