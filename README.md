# weather-telegram-bot
Телеграмм-бот, рассказывающий о погоде.
Написан на python.

Применяются техники NLP для извлечения городов в их начальной форме и дат из текстов пользователя
(пакет natasha для NLP на русском языке).

Для получения координат города по его названию используется
[Yandex API для перевода географических координат в адрес и наоборот](https://yandex.ru/dev/maps/geocoder/). <br>
Для получения прогноза погоды по полученным координатам используется [Open Weather API](https://openweathermap.org/forecast5).

## Навигация
- [Что умеет бот](#что-умеет-бот)
- [Используемые библиотеки](#используемые-библиотеки)
- [Запуск бота](#запуск-бота)
- [Полезные ссылочки с tutorial по написанию бота](#полезные-ссылочки-с-tutorial-по-написанию-бота)
- [Почему выбрана python-telegram-bot библиотека](#почему-выбрана-python-telegram-bot-библиотека)
 
## Что умеет бот:
- Умеет говорить погоду в ЛЮБОМ городе России (за исключением каких-то мелких городов, о которых не знает API яндекса или open weather).
- Бот умеет извлекать названия городов и приводить их названия в начальную форму (чтобы потом получить координаты данного города).
- Бот умеет извлекать даты и приводит их единому формату (далеко не идеально, но справляется с многими кейсами).
- На основе извлеченного названия города бот умеет давать прогноз погоды на нужную дату (в пределах 5 дней вперед).
- Бот умеет здороваться, прощаться.
- Бот умеет реагировать на непонятные высказывания.
- Бот должен работать и продолжать вас что-то спрашивать пока вы не закончите беседу.

## Используемые библиотеки
Перед запуском проекта необходимо установить следующие пакеты:
- **python-telegram-bot** - библиотека-обертка для работы с api телеграмма ([подробнее здесь](#почему-выбрана-python-telegram-bot-библиотека))
- **natasha** - библиотека для nlp при работе с русским текстом ([подробнее здесь](https://habr.com/ru/post/516098/))
- **emoji** - пригодится для работы со смайликами
- **requests** - для работы с Api Yandex и API Open Weather

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
    + в константе `OPEN_WEATHER_API_TOKEN` подставь токен для [Open Weather API](https://openweathermap.org/api). <br>

3. Запусти скрипт в корне репозитория `weather_bot.py`
    
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