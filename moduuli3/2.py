userInput = input("Laivan hyttiluokka: ")

if userInput == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")

elif userInput == "a":
    print("A on ikkunallinen hytti autokannen yläpuolella.")

elif userInput == "b":
    print("B on ikkunaton hytti autokannen yläpuolella.")

elif userInput == "c":
    print("C on ikkunaton hytti autokannen alapuolella.")

else:
    print("Virheellinen syöttö!")
