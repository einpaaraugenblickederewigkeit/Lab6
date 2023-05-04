import requests

city = input("Введите город: ")

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=d2abe737dccf6a8c199c4d475f87a0e1&units=metric&lang=ru' #Адрес запроса с моим ключем на OpenWeatherMap 
response = requests.get(url)

if response.status_code == 200: #Если код ответа равен 200, значит данные получены, и можно из json файла вынимать нужную информацию
    data = response.json()
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    wind_speed = data['wind']['speed']
    description = data['weather'][0]['description']
    print(f"Текущая погода в {city}:")
    print(f"Температура: {temp} °C")
    print(f"Ощущается как: {feels_like} °C")
    print(f"Скорость ветра: {wind_speed} м/с")
    print(f"На небе {description}")
else:
    print("Ошибка при получении данных о погоде")

