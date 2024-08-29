numerot = []

userInput = (input("Anna luku: "))

while userInput != "":
    convert = int(userInput)
    numerot.append(convert)
    userInput = (input("Anna luku: "))

else:
    print("")
    print("Syötit tyhjän merkkijonon!")
    print("")
    print("Isoin luku:", int(max(numerot)))
    print("Pienin luku:", int(min(numerot)))




