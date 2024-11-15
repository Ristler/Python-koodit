
import requests


##APIKEY POISTETTU


paikkakunta = input("Anna paikkakunta: ")
pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid&units=metric"

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        print(json_vastaus["weather"][0]["main"])
        print(json_vastaus["main"]["temp"], "°C")
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")
