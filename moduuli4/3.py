numerot = ([])

userInput = (input("Anna luku: "))

while userInput != "":
    numerot.append(userInput)
    userInput = (input("Anna luku: "))

else:
    print("")
    print("Syötit tyhjän merkkijonon!")
    print("")
    print("Isoin luku:", max(numerot))
    print("Pienin luku:", min(numerot))




