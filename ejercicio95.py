# 95.- API Clima Open-Meteo
import requests

# CDMX aprox
lat = 19.43
lon = -99.13
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

resp = requests.get(url)
data = resp.json()

clima = data['current_weather']
print("Temperatura:", clima['temperature'])
print("Viento:", clima['windspeed'])