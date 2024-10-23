
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

    def kulje(self, tuntimaara):
        self.kuljettumatka = self.kuljettumatka + self.nopeus * tuntimaara
        return


auto = Auto("ABC-123", 142)


print(f"Rekisterinumero: {auto.rekisterinumero}\n"
      f"Huippunopeus: {auto.huippunopeus} km/h\n"
      f"Nopeus: {auto.nopeus}\n"
      f"Kuljettumatka: {auto.kuljettumatka}")


auto.kiihdytä(60)
auto.kulje(1.5)
print("Auton nopeus nyt:", auto.nopeus)

print("Auton kuljettumatka on:", auto.kuljettumatka)

