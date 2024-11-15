import random
i = 1
carid = 0
autot = []

class Auto:
    def __init__(self, rekisterinumero, huippunopeus, nopeus = 0, kuljettumatka = 0):
        self.rekisterinumero = rekisterinumero
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettumatka = kuljettumatka

    def kiihdytä(self, kmh):
        self.nopeus += kmh
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tuntimaara):
        self.kuljettumatka = self.kuljettumatka + self.nopeus * tuntimaara
        return

while i <= 10:
    auto = Auto(f"ABC-{i}", random.randint(100, 200))
    autot.append(auto)
    i = i + 1

class Kilpailu:
    def __init__(self, nimi, pituus, autot=[]):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        tunti = 0
        while True:
            for auto in autot:
                auto.kiihdytä(random.randint(-10, 15))
                auto.kulje(1)
            tunti+=1
            if tunti % 10 == 0:
                self.tulosta_tilanne()
            if self.kilpailu_ohi() == True:
                return

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettumatka >= self.pituus:
                print("Voittajan auto: ", vars(auto))
                return True
        return False

    def tulosta_tilanne(self):
        for auto in autot:
            print("")
            print(f"Rekisterinumero: {auto.rekisterinumero}\n"
                  f"Huippunopeus: {auto.huippunopeus} km/h\n"
                  f"Nopeus: {auto.nopeus}\n"
                  f"Kuljettumatka: {auto.kuljettumatka}")
            print("-----------------------")
        return

romuralli = Kilpailu("Suuri romuralli", 8000, autot)
romuralli.tunti_kuluu()
romuralli.tulosta_tilanne()

