from flask import Flask, Response
import mysql.connector
import json
app = Flask(__name__)

@app.route('/ICAO/<code>')

def fetch(code):
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='salasana',
        autocommit=True
    )
    sql = f"SELECT ident, name, municipality FROM airport where ident='{code}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount > 0:
        for rivi in tulos:
            name = rivi[1]
            municipality = rivi[2]

    vastaus = {
        "ICAO": code, "Name:": name, "Municipality:": municipality
    }
    return vastaus

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)