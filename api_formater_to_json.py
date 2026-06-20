import json
from datetime import datetime

import requests


def get_weather(latitude: float, longitude: float) -> dict:
    """
    Получение текущей погоды из Open-Meteo API.
    """

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "apparent_temperature",
            "wind_speed_10m",
            "weather_code"
        ]
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    return response.json()


def save_to_json(data: dict, filename: str) -> None:
    """
    Сохранение данных в JSON-файл.
    """

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    # Координаты Москвы
    latitude = 55.7558
    longitude = 37.6176

    weather_data = get_weather(latitude, longitude)

    filename = f"weather_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    save_to_json(weather_data, filename)

    print(f"Данные успешно сохранены в файл {filename}")


if __name__ == "__main__":
    main()