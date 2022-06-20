import requests
from pprint import pprint
import datetime as dt
from config import open_weather_token

def get_weather(city):
    global open_weather_token
    try:
        r=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric')
        data=r.json()
        # pprint(data)

        city_1=data['name']
        cur_weather=data['main']['temp']
        humidity=data['main']['humidity']
        pressure=data['main']['pressure']
        wind=data['wind']['speed']
        sunrise_time=dt.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_time=dt.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day=dt.datetime.fromtimestamp(data['sys']['sunset'])-dt.datetime.fromtimestamp(data['sys']['sunrise'])
        res=f'***{dt.datetime.now().strftime("%Y-%m-%d")}***\n' \
            f'Погода в городе {city_1}\nТемпература: {cur_weather}C°\nВлажность: {humidity}%\n' \
            f'Давление: {pressure} мм.рт.ст.\nСкорость ветра: {wind} м/с.\n' \
            f'Восход солнца: {sunrise_time}\nЗакат солнца: {sunset_time}\n' \
            f'Продолжительность дня: {length_of_the_day}'
        print(res)
        return res
    except Exception as ex:
        print(ex)
        print('Проверьте название города:')
        return 'Неверное название города, повторите попытку.'


# def main():
#     city=input('Введите город:')
#     get_weather(city,open_weather_token)

