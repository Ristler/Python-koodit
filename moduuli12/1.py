import requests
import json
pyyntö = "https://api.chucknorris.io/jokes/random"

vastaus = requests.get(pyyntö)
json_vastaus = vastaus.json()
print("")
print(json_vastaus["value"])


