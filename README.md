# weather-telegram-bot
Телеграмм-бот, рассказывающий о погоде. Написана на python с использованием библиотеки python-telegram-bot.

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