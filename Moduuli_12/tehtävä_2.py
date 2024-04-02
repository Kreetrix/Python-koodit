import requests


api = "b6918ea857c69fc27fd09fb8c40568e4"
x = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=Espoo&appid={api}')


print(x.text)