from random import randint


def noppa():
    random = randint(1, 6)
    return random

numero = 0

while numero != 6:
    numero = noppa()
    print(numero)



