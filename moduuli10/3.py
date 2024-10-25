class Hissi:
    def __init__(self, alin, ylin, kerros=0):
        self.kerros = kerros
        self.ylin = ylin
        self.alin = alin

    def kerros_ylös(self, input):
        for i in range(input - self.kerros):
            self.kerros += 1
            if self.kerros > self.ylin:
                self.kerros = self.ylin
                print(
                    "Ilmoitus: yritit mennä liian ylös, kyseistä kerrosta ei löydy. Hissi on kuitenkin ylimmässä kerroksessa.")
                break
            print(f"Noustaan kerros.. {self.kerros}")
        return

    def kerros_alas(self, input):
        for i in range(self.kerros - input):
            self.kerros -= 1
            if self.kerros < self.alin:
                self.kerros = self.alin
                print(
                    "Ilmoitus: yritit mennä liian alas, kyseistä kerrosta ei löydy. Hissi on kuitenkin alhaisemmassa kerroksessa.")
                break
            print(f"Mennään kerros alaspäin.. {self.kerros}")
        return

    def siirry_kerrokseen(self, input):
        if input >= self.kerros:
            self.kerros_ylös(input)
        elif input <= self.kerros:
            self.kerros_alas(input)
        return

class Talo:
    def __init__(self, alin, ylin, hissienmaara):
        self.hissit = []
        self.alin = alin
        self.ylin = ylin
        self.hissienmaara = hissienmaara
        for i in range(hissienmaara):
            print(f"Hissi {i} lisätty.")
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissia(self, numero, kohde):
        self.hissit[numero - 1].siirry_kerrokseen(kohde)


    def palohalytys(self):
        print("PALOHÄLYTYS")
        for hissi in self.hissit:
            hissi.kerros_alas(self.alin)
        return

    ##Only used for testing
    def hissiStatus(self):
        for hissi in self.hissit:
            print(vars(hissi))


talo = Talo(-6, 10, 3)
talo.aja_hissia(1, 6)
talo.hissiStatus()
talo.palohalytys()
talo.hissiStatus()

