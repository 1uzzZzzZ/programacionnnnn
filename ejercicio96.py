# 96.- API PokeAPI Pikachu
import requests

url = "https://pokeapi.co/api/v2/pokemon/25"
resp = requests.get(url)
poke = resp.json()

print("Nombre:", poke['name'])
print("Tipos:")
for t in poke['types']:
    print("-", t['type']['name'])