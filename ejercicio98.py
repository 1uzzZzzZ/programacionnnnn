# 98.- Dictionary API
import requests

palabra = "example"
url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{palabra}"

resp = requests.get(url)
datos = resp.json()

# La respuesta es una lista, tomamos el primer elemento
item = datos[0]
definicion = item['meanings'][0]['definitions'][0]['definition']

print("Palabra:", palabra)
print("Definicion:", definicion)