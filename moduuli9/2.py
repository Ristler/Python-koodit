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

auto = Auto("ABC-123", 142)
print(f"Rekisterinumero: {auto.rekisterinumero}\n"
      f"Huippunopeus: {auto.huippunopeus} km/h\n"
      f"Nopeus: {auto.nopeus}\n"
      f"Kuljettumatka: {auto.kuljettumatka}")

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print("Auton nopeus nyt:", auto.nopeus)
auto.kiihdytä(-200)

print("Auton nopeus nyt jarruttaessa:", auto.nopeus)
