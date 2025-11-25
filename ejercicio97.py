# 97.- Guardar JSON en archivo
import requests
import json

url = "https://api.github.com"
resp = requests.get(url)
datos = resp.json()

with open("respuesta.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=4)

print("Datos guardados en respuesta.json")