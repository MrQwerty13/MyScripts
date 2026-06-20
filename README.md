# WeatherPiServer

Серверная часть проекта WeatherPi.

## Возможности

- получение данных о погоде;
- сохранение архива JSON;
- REST API;
- хранение истории наблюдений.

## Структура

- collector — получение данных
- api — REST API
- shared — общие модули
- data — архив JSON
- logs — журнал работы

## Установка

```bash
python -m venv .venv
```

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

Запуск:

```bash
python main.py
```