from random import randint

numero = 0

def noppa():
    random = randint(1, 6)
    return random

while numero != 6:
    numero = noppa()
    print(numero)



