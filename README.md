# __Detective Announcer Bot__ 🕵

Бот, предназначенный для пересылки записей со стены сообщества [Alibi](https://vk.com/alibigames) и [Detectit](https://vk.com/detectitspb) в выбранный телеграм чат/канал, создания более удобной системы опросов для выбора игрового дня, чем это может предложить Telegram, а также ведения в чате истории побед команды.
___
### Возможности
💨 Мгновенная пересылка новых записей со стены VK в телеграм чат.

🚨 Получение уведомления в телеграм чате от организации об успешной регистрации команды на игре.

📈 Сохранение истории побед (для игр, в которой команда заняла 1-5 место).

🙋‍♀️ Автоматическое создание наглядного сообщения-опроса с кнопками, содержащего вакантные игровые даты предстоящей игры с подробной информацией.

![buttons_preview](https://github.com/TheSuncatcher222/detective_announcer_bot/assets/36377190/b0da3621-b443-491f-bcb7-bf053a4c2aab)

___
### Технологии

[Python] - целевой язык программирования.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

[Telegram API] - набор готовых классов, процедур, функций, структур и констант, предоставляемых социальной сетью Telegram, которые позволяют взаимодействовать с ее базой данных с помощью http-запросов.

![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)

[VK API] - набор готовых классов, процедур, функций, структур и констант, предоставляемых социальной сетью VK (ВКонтакте), которые позволяют взаимодействовать с ее базой данных с помощью http-запросов.

![Вконтакте](https://img.shields.io/badge/вконтакте-%232E87FB.svg?&style=for-the-badge&logo=vk&logoColor=white)
___

### Установка

✅ Создать телеграм-бота согласно [официальной инструкции ](https://core.telegram.org/bots).

✅ Получить VK токен по [ссылке ](https://vkhost.github.io/)

_Стоит выбрать токен VK.com. Однако в случае возникновения ошибок (например, API VK: vk_api.exceptions.ApiError: [3] Unknown method passed) необходимо выбрать токен VK Admin._

✅ Перейти в целевую папку проекта и клонировать репозиторий
```sh
git clone https://github.com/TheSuncatcher222/Detective_Announcer_Bot.git
cd Detective_Announcer_Bot
```

✅ Создать виртуальное окружение

> Windows

```sh
python -3.9 -m venv venv
```

> Linux

```sh
python3 -m venv venv
```

> MacOS

```sh
brew link python@3.9
```

✅ Активировать виртуальное окружение

```sh
source venv/scripts/activate
```

✅ Обновить инсталлятор pip

```sh
python -m pip install --upgrade pip
```

✅ Установить зависимости из requirements.txt

```sh
pip install -r requirements.txt
```

✅ Перейти в папку с данными для подключения к API
```
cd project/data
```

✅ Переименовать файл .env.example в .env и заполнить его согласно примеру

```
# Нижеуказанный код приведен для консоли Bash:
mv .env.example .env
nano .env
```

✅ Вернуться в корневую папку и запустить сервер

```sh
cd ../..
python main.py
```
___
### Лицензия

MIT 
**Free Software, Hell Yeah!**

Created by [TheSuncatcher222](https://github.com/TheSuncatcher222)

Данный бот __не является__ официальным!


[Alibi]: <https://vk.com/alibigames>
[Python]: <https://www.python.org/>
[VK API]: <https://dev.vk.com/api/overview>
[Telegram API]: <https://core.telegram.org/bots/api>
