# Импортируем все что нужно
import tkinter as tk
from tkinter import Entry, Label, Button, BOTTOM
from PIL import Image, ImageTk
from io import BytesIO
import requests
import json

def get_weather_data(city):
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&APPID=4e04ad39dd9272d1ae0b831946a29bc4'
        weather_data = requests.get(url).json()
        return weather_data
    except Exception as e:
        print(f"Ошибка при получении данных о погоде: {e}")
        return None

def update_gui(weather_data):
    if weather_data:
        temperature = round(weather_data['main']['temp'])
        temperature_feels = round(weather_data['main']['feels_like'])
        wind_speed = round(weather_data['wind']['speed'])
        
        city_label.config(text=f'Ваш город: {city}.')
        temperature_label.config(text=f'Сейчас в городе {temperature} °C')
        temperature_feels_label.config(text=f'Ощущается как {temperature_feels} °C')
        wind_speed_label.config(text=f'Скорость ветра {wind_speed} м/с')

        # Добавляем вывод иконки погоды
        icon_url = f'http://openweathermap.org/img/w/{weather_data["weather"][0]["icon"]}.png'
        icon_data = requests.get(icon_url)
        icon_image = Image.open(BytesIO(icon_data.content))
        # Изменение размера изображения (например, до 50x50 пикселей)
        new_size = (80, 80)
        icon_image = icon_image.resize(new_size, Image.LANCZOS)
        icon_image = ImageTk.PhotoImage(icon_image)

        icon_label.config(image=icon_image)
        icon_label.image = icon_image

def get_city():
    global city
    city = city_entry.get()
    weather_data = get_weather_data(city)
    update_gui(weather_data)

root = tk.Tk()
root.title('Погода')
root.geometry('400x500')
root.iconphoto(False, tk.PhotoImage(file='img/logo.png'))

city = 'Томск'
city_label = Label(root, text=f'Ваш город: {city}.', font=35)
city_label.pack(pady=(20, 0))

city_entry = Entry(root, font=35)
city_entry.insert(0, 'Томск')  # Установка дефолтного значения
city_entry.pack(pady=(10, 0))

city_button = Button(root, text='Выбрать город', font=40, command=get_city)
city_button.pack(pady=(10, 0))

temperature_label = Label(root, text='Сейчас в городе', font=35)
temperature_label.pack(pady=(10, 0))
temperature_feels_label = Label(root, text='Ощущается как', font=35)
temperature_feels_label.pack(pady=(10, 0))
wind_speed_label = Label(root, text='Скорость ветра', font=35)
wind_speed_label.pack(pady=(10, 0))

# Инициализируем метку для иконки погоды
icon_label = Label(root)
icon_label.pack(pady=(10, 0))

button = Button(root, text='Узнать погоду', font=40, command=get_city)
button.pack(side=BOTTOM, pady=40)

root.mainloop()

# Видео в помощь
# https://www.youtube.com/watch?v=UDFlI4ZmM38

# print('Сейчас в городе', city, str(temperature), 'градусов')
# print('Ощущается как', str(temperature_feels), 'градусов')
# print('Скорость ветра', str(wind_speed), 'м/с')