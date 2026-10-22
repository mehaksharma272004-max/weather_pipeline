import requests
import pandas as pd

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 28.6139,
    "longitude": 77.2090,
    "current": "temperature_2m,relative_humidity_2m,apparent_temperature",
    "timezone": "auto"
}

response = requests.get(url, params=params)
response.raise_for_status()

weather = response.json()
print("Weather data received successfully!")
print(weather["current"])
