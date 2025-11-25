# 94.- Status code GitHub
import requests

url = "https://api.github.com"
resp = requests.get(url)

print("Codigo de estado:", resp.status_code)
if resp.status_code == 200:
    print("Todo bien")