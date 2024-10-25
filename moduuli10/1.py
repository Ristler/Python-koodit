class Hissi:
    def __init__(self, ylin, alin, kerros = 0):
        self.kerros = kerros
        self.ylin = ylin
        self.alin = alin

    def kerros_ylös(self, input):
        for i in range(input - self.kerros):
            self.kerros +=1
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
                print("Ilmoitus: yritit mennä liian alas, kyseistä kerrosta ei löydy. Hissi on kuitenkin alhaisemmassa kerroksessa.")
                break
            print(f"Mennään kerros alaspäin.. {self.kerros}")
        return

    def siirry_kerrokseen(self, input):
        if input >= self.kerros:
            self.kerros_ylös(input)
        elif input <= self.kerros:
            self.kerros_alas(input)
        return

hissi = Hissi(10, -2)
hissi.siirry_kerrokseen(10)
hissi.siirry_kerrokseen(-3)

print("Hissin kerros nyt siirtymän jälkeen:", hissi.kerros)