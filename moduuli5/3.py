

userInput = int(input("Anna luku: "))

while userInput % userInput == 0 and userInput % 1 == 0:
    print("On alkuluku")
    userInput = int(input("Anna luku: "))

else:
    print("Ei ole")


