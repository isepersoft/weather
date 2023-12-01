# Импортируем все что нужно
import tkinter as tk
import requests
import json

from tkinter import *

def weather():
    url = ('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&APPID=4e04ad39dd9272d1ae0b831946a29bc4')

    weather_data = requests.get(url).json()
    weather_data_structure = json.dumps(weather_data, indent=2)

    temperature = round(weather_data['main']['temp'])
    temperature_feels = round(weather_data['main']['feels_like'])
    wind_speed = round(weather_data['wind']['speed'])
    
    city_label.config(text='Ваш город: '+ str(city) +'.')
    temperature_label.config(text='Сейчас в городе ' + str(temperature) + ' °C')
    temperature_feels_label.config(text='Ощущается как ' + str(temperature_feels) + ' °C')
    wind_speed_label.config(text='Скорость ветра ' + str(wind_speed) + ' м/с')

root = Tk()


root.title('Погода')
root.geometry('300x400')
root.iconphoto(False, tk.PhotoImage(file='img/logo.png'))

city = 'Томск'
city_label = Label(root, text='Ваш город: '+ str(city) +'.', font=35)
city_label.pack(pady=(50, 0))

temperature_label = Label(root, text='Сейчас в городе', font=35)
temperature_label.pack(pady=(10, 0))
temperature_feels_label = Label(root, text='Ощущается как', font=35)
temperature_feels_label.pack(pady=(10, 0))
wind_speed_label = Label(root, text='Скорость ветра', font=35)
wind_speed_label.pack(pady=(10, 0))

button = Button(root, text='Нажми чтобы узнать', font=40, command=weather)
button.pack(side=BOTTOM, pady=40)


root.mainloop()

# Видео в помощь
# https://www.youtube.com/watch?v=UDFlI4ZmM38

# print('Сейчас в городе', city, str(temperature), 'градусов')
# print('Ощущается как', str(temperature_feels), 'градусов')
# print('Скорость ветра', str(wind_speed), 'м/с')