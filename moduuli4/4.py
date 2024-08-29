
from random import randint

oikein = randint(1, 10)
userInput = int(input("Arpapeli!: "))

while userInput != oikein:
    if userInput < oikein:
        print("Liian pieni arvaus")
    elif userInput > oikein:
        print("Liian suuri vastaus")
    userInput = int(input("Arpapeli!: "))

if userInput == oikein:
    print("")
    print("Oikein!")




