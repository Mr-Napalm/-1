import requests
from datetime import datetime #подключаем библиотеки
city="Moscow,RU"
appid="7a67813b29831e0d5724f9661a1efe0f"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid}) # делаем запрос на сервис
data = res.json()  # создаем список с данными

print("Город:", city) # отображаем наши данные
print(datetime.now().date())
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Скорость ветра", data['wind']['speed'])
print("Видимость",data["visibility"])
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("\r\n")
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <",i['main']['temp'], "> \r\nПогодные условия <"
          ,i['weather'][0]['description'], ">" "\r\nСкорость ветра <", i["wind"]["speed"],"> "
        "\r\nВидимость <",i["visibility"], ">")
    print("_____________________")
