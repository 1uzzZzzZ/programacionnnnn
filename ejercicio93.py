# 93.- API Numbers trivia
import requests

url = "http://numbersapi.com/42?json"
respuesta = requests.get(url)
datos = respuesta.json()

print("Trivia del 42:", datos['text'])