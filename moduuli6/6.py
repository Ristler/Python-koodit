import math
pizza1 = 0
pizza2 = 0

def pizzaprice (p, e):
    sade = p / 2
    answer = (math.pi * sade * sade) / 10000
    final = answer
    return e / final

cm = int(input("Anna pizzan halkaisija: "))
eur = int(input("Anna pizzan hinta: "))
pizza1 = pizzaprice(cm, eur)

cm = int(input("Anna pizzan halkaisija: "))
eur = int(input("Anna pizzan hinta: "))
pizza2 = pizzaprice(cm, eur)

if pizza1 > pizza2:
    print("Toka pizza on parempi, get it!")
    print("")
    print("Ekan pizzan Yksikköhinta: ", pizza1, "Euroa")
    print("Tokan pizzan Yksikköhinta: ", pizza2, "Euroa")
if pizza2 > pizza1:
    print("Eka pizza on parempi, get it!")
    print("")
    print("Ekan pizzan Yksikköhinta: ", round(pizza1), "Euroa.")
    print("Tokan pizzan Yksikköhinta: ", round(pizza2), "Euroa.")
