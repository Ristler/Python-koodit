
def convert(x):
    return x * 3.785

userInput = float(input("Gallons To Gas: "))
nro = float(userInput)

while nro > 0:
    print(convert(nro), "Liters")
    userInput = float(input("Gallons To Gas: "))
    nro = float(userInput)
else:
    print("Bye")




