class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Julkaisu: {self.nimi}")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja: {self.kirjoittaja}\n"
              f"Sivumäärä: {self.sivumäärä}")

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja: {self.päätoimittaja}")


print("")
magazine = Lehti("Aku Ankka", "Aki Hyyppä")
book = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

Lehti.tulosta_tiedot(magazine)
print("")
Kirja.tulosta_tiedot(book)
