from audioop import reverse
lista = []

userInput = (input("Kirjoita luku: "))

while userInput != "":
    convert = int(userInput)
    lista.append(convert)
    userInput = (input("Kirjoita luku: "))
else:
    largest = sorted(lista, reverse=True)[:5]
    print("Viisi suurinta lukua järjestyksessä:", largest)

