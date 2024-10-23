import random;
i = 1
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

def vroom():
    while True:
        for auto in autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)

            if auto.kuljettumatka >= 10000:
                print("")
                print("Voittaja on:")
                print("")
                print(f"Rekisterinumero: {auto.rekisterinumero}\n"
                      f"Huippunopeus: {auto.huippunopeus} km/h\n"
                      f"Nopeus: {auto.nopeus}\n"
                      f"Kuljettumatka: {auto.kuljettumatka}")
                print("-----------------------")
                print("")
                for auto in autot:
                    print("")
                    print(f"Rekisterinumero: {auto.rekisterinumero}\n"
                          f"Huippunopeus: {auto.huippunopeus} km/h\n"
                          f"Nopeus: {auto.nopeus}\n"
                          f"Kuljettumatka: {auto.kuljettumatka}")
                    print("-----------------------")
                exit()
vroom()











