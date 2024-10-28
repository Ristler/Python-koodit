
import requests

paikkakunta = input("Anna paikkakunta: ")
pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid=a89956b7488968e2882bae86106eb1b6&units=metric"

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        print(json_vastaus["main"]["temp"], "°C")
        print(json_vastaus["weather"][0]["main"])
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")