import requests
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('.env')  # path to .env file
load_dotenv(dotenv_path=dotenv_path)  # load the .env file

TOKEN = os.getenv('TOKEN')
units = 'metric'

city = input("Input your city name: ")
weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={TOKEN}&units={units}')

print(weather.text)
print(f'Temperature -> {weather.json()['main']['temp']}')
