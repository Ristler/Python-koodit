
import mysql.connector
heliports = []
smallAirports = []
mediumAirports = []
closed = []

def getAirport(code):
    sql = f"SELECT airport.type FROM airport where airport.iso_country='{code}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount > 0:
        for rivi in tulos:
            if "heli" in rivi[0]:
                heliports.append(rivi[0])
            if "small" in rivi[0]:
                smallAirports.append(rivi[0])
            if "medium" in rivi[0]:
                mediumAirports.append(rivi[0])
            if "closed" in rivi[0]:
                closed.append(rivi[0])
    return

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='salasana',
    autocommit=True
)
code = input("Anna maakoodi: ")
getAirport(code)
print("Heliports:", len(heliports))
print("SmallAirports:", len(smallAirports))
print("MediumAirports:", len(mediumAirports))
print("All:",len(heliports+smallAirports+mediumAirports+closed) )