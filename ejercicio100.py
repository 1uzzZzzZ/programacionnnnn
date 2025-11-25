# 100.- Lista de primeros 5 Pokemon
import requests

url = "https://pokeapi.co/api/v2/pokemon?limit=5"
resp = requests.get(url)
data = resp.json()

lista_pokemon = data['results']

print("--- Primeros 5 Pokemon ---")
for p in lista_pokemon:
    print(p['name'])