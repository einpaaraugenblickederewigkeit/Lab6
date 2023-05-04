import requests

# параметры запроса
url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    'q': 'Moscow',  # наименование города
    'appid': 'd2abe737dccf6a8c199c4d475f87a0e1',  # API-ключ
    'units': 'metric'  # система измерения (метрическая)
}

# выполнение запроса
response = requests.get(url, params=params)

# проверка статуса ответа
if response.status_code == 200:
    # получение данных о погоде
    weather = response.json()
    print(f"Текущая температура в городе {weather['name']}: {weather['main']['temp']} градусов Цельсия")
else:
    # обработка ошибки
    print("Ошибка при выполнении запроса")
    print(response.status_code)


