class Auto:
    def __init__(self, rekisterinumero, huippunopeus, nopeus = 0, kuljettumatka = 0):
        self.rekisterinumero = rekisterinumero
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettumatka = kuljettumatka

auto = Auto("ABC-123", 142)
print(f"Rekisterinumero: {auto.rekisterinumero}\n"
      f"Huippunopeus: {auto.huippunopeus} km/h\n"
      f"Nopeus: {auto.nopeus}\n"
      f"Kuljettumatka: {auto.kuljettumatka}")