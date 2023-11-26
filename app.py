# Импортируем все что нужно
import tkinter as tk
import requests
import json

from tkinter import *


city = 'Томск'

url = ('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&APPID=4e04ad39dd9272d1ae0b831946a29bc4')

weather_data = requests.get(url).json()
weather_data_structure = json.dumps(weather_data, indent=2)

temperature = round(weather_data['main']['temp'])
temperature_feels = round(weather_data['main']['feels_like'])
wind_speed = round(weather_data['wind']['speed'])

print('Сейчас в городе', city, str(temperature), 'градусов')
print('Ощущается как', str(temperature_feels), 'градусов')
print('Скорость ветра', str(wind_speed), 'м/с')


