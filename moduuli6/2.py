from random import randint

numero = 0
userInput = int(input("Nopan maksimisilmäluku: "))

def noppa(x):
    random = randint(1, x)
    return random

while numero != userInput:
    numero = noppa(21)
    print(numero)

