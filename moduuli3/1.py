userInput = float(input("Kuhan pituus: "))

if userInput<37:
    print("Päästä kuha takaisin järveen.")
    print("Kuha on liian pieni:",37 - userInput, " cm.")

elif userInput>=37:
    print("Onneksi olkoon!")