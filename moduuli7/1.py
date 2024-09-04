
kuukaudet = ("tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu")
kuukausinro = int(input("Anna kuukauden numero: "))

while kuukausinro != 0:
    if kuukausinro == 3 or kuukausinro == 4 or kuukausinro == 5:
        print("Kevät")
        kuukausinro = int(input("Anna kuukauden numero: "))

    elif kuukausinro == 6 or kuukausinro == 7 or kuukausinro == 8:
        print("Kesä")
        kuukausinro = int(input("Anna kuukauden numero: "))

    elif kuukausinro == 9 or kuukausinro == 10 or kuukausinro == 11:
        print("Syksy")
        kuukausinro = int(input("Anna kuukauden numero: "))

    elif kuukausinro == 2 or kuukausinro == 1 or kuukausinro == 12 :
        print("Talvi")
        kuukausinro = int(input("Anna kuukauden numero: "))



