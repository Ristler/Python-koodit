vuosi = float(input("Syötä vuosi, tarkistan onko se karkausvuosi: "))

if vuosi % 400 == 0:
    print("On karkauvuosi")

elif vuosi % 100 == 0 and vuosi % 400 == 0:
    print("On karkausvuosi")

else:
    print("Ei ole karkausvuosi")

