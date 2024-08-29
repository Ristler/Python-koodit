
from random import randint

userInput = int(input("Arpakuution lukumäärä: "))
nopat = 0

for _ in range(userInput):

    random = randint(1, 6)
    nopat = nopat + random
print("Silmälukujen summa:", nopat)








