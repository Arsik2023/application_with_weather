#  https://docs.python.org/3/library/json.html - если что-то непонятно
import requests
import json  #нужен для расшифрования в удобный формат

class Requests:
    def __init__(self):
        pass
    def Requests(self):
        self.city = 'Екатеринбург'
        parameters = {
            'lang': 'ru'
        }
        url = ('https://api.openweathermap.org/data/2.5/weather?q='+self.city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347')
        weather_data = requests.get(url).json()  # json() - преобразование в объект
        #  Метод GET указывает на то, что происходит попытка извлечь данные из определенного ресурса
        weather_data_structure = json.dumps(weather_data, indent=1)  # dump преобразовывает словарь в строку
        wind_speed = int(round(weather_data['wind']['speed']))
        temperature = int(round(weather_data['main']['temp'], 0))
        weather = weather_data['weather']
        weather = weather[0]['description'].lower()
        return [temperature, wind_speed, weather]
""" Ekaterinburg = Requests()
print(Ekaterinburg.Requests()) """
