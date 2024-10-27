
class Auto:
    def __init__(self, rekisterinumero, huippunopeus, nopeus = 0, kuljettumatka = 0):
        self.rekisterinumero = rekisterinumero
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettumatka = kuljettumatka

    def tulosta_tiedot(self):
        print(f"Auto: {self.rekisterinumero}\n"
              f"Huippunopeus {self.huippunopeus}\n"
              f"Nopeus: {self.nopeus}\n"
              f"Matkamittari: {self.kuljettumatka} KM")

    def kiihdytä(self, kmh):
        self.nopeus += kmh
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tuntimaara):
        self.kuljettumatka = self.kuljettumatka + self.nopeus * tuntimaara
        return

class Sähköauto(Auto):
    def __init__(self, rekisterinumero, huippunopeus, akku):
        self.akku = akku
        super().__init__(rekisterinumero, huippunopeus)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Akku: {self.akku} KWH")


class Polttomoottoriauto(Auto):
    def __init__(self, rekisterinumero, huippunopeus, tankki):
        self.tankki = tankki
        super().__init__(rekisterinumero, huippunopeus)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Polttoainetankki: {self.tankki} L")


bmwi4 = Sähköauto("ABC-15", 180, 52.5)
volvoV50 = Polttomoottoriauto("ACD-123", 165, 32.3)
bmwi4.kiihdytä(120)
volvoV50.kiihdytä(150)
bmwi4.kulje(3)
volvoV50.kulje(3)
print("")
Sähköauto.tulosta_tiedot(bmwi4)
print("")
Polttomoottoriauto.tulosta_tiedot(volvoV50)

