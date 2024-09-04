
lentoasemat = {}

def menu():
    print("-----------------------------------")
    print("Valitse seuraavista vaihtoehdoista.")
    print("-----------------------------------")
    x = int(input("1. Uusi lentoasema""\n2. Hae lentoasemaa""\n3. Lopeta""\n""\nValinta: "))
    return x

def addAirport():
    print("")
    code = str(input("ICAO-koodi: "))
    name = str(input("Lentoaseman nimi: "))
    lentoasemat[code.upper()] = name
    return

def findairport():
    print("")
    code = str(input("ICAO-koodi: "))
    upper = code.upper()
    print("")
    if upper in lentoasemat:
        lentokentta = lentoasemat[upper]
        return print("Löydetty lentokenttä:",lentokentta)
    if code not in lentoasemat:
        return print("Lentokenttää ei löydy.")

while True:
    choice = menu()
    if choice== 1:
        addAirport()
    elif choice == 2:
        findairport()
    elif choice == 3:
        print("Sammutetaan ohjelmaa..")
        break



