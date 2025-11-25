# 99.- Input usuario y API Numbers
import requests

num = input("Ingresa un numero entero: ")
url = f"http://numbersapi.com/{num}?json"

resp = requests.get(url)
if resp.status_code == 200:
    data = resp.json()
    print("Dato curioso:", data['text'])
else:
    print("No encontre datos para ese numero.")