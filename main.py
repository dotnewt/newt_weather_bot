import requests
from pprint import pprint
import datetime
from config import open_weather_token


def get_weather(city, open_weather_token):

    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        'Drizzle': "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
           f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
           wd = code_to_smile[weather_description]
        else:
           wd = "ХЗ, сам встань и посмотри в окно))"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        
        print(f"Weather in {city}: \n {cur_weather}C° {wd} \n {humidity} \n {pressure} \n {wind} \n {sunset_timestamp}")
    
    except Exception as ex:
        print(ex)
        print("Проверьте название города ")


def main():
    city = input("Введите город: ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
