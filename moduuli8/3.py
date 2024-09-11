import mysql.connector
from geopy.distance import geodesic

x = []

def getAirport(code):
    sql = f"SELECT airport.latitude_deg, airport.longitude_deg FROM airport where ident='{code}'"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount > 0:
        for rivi in tulos:
            x.append(rivi[0])
            x.append(rivi[1])
    return

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='salasana',
    autocommit=True
)
code = input("Anna ICAO koodi: ")
getAirport(code)
code = input("Anna ICAO koodi: ")
getAirport(code)

print("Etäisyys on: ", geodesic((x[0], x[1]), (x[2], x[3])).km, "KM.")

