import mysql.connector


def getAirport(code):
    sql = f"SELECT ident, name FROM airport where ident='{code}'"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
 
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f" {rivi[1]}")
    return

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='salasana',
         autocommit=True
         )
code = input("Anna ICAO koodi: ")
getAirport(code)