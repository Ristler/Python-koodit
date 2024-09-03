
userInput = int(input("Anna luku: "))


for _ in range(2, userInput):
    if userInput % 1 == 0 and userInput % userInput == 0:
        print("On alkuluku")
else:
    print("Ei ole")





