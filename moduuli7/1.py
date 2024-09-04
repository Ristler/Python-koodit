#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
#jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan
#(kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat
#vuodenajat merkkijonoina
#monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
#että joulukuu on ensimmäinen talvikuukausi.

kuukaudet = ("tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu")
kuukausinro = int(input("Anna kuukauden numero: "))
vuodenaika = "tammikuu"


while kuukausinro != 0:

    if kuukausinro <= 3:
        print("Kevät")
        kuukausinro = int(input("Anna kuukauden numero: "))


    elif kuukausinro <= 6:
        print("Kesä")
        kuukausinro = int(input("Anna kuukauden numero: "))


    elif kuukausinro <= 9:
        print("Syksy")
        kuukausinro = int(input("Anna kuukauden numero: "))

    elif kuukausinro <= 12:
        print("Talvi")
        kuukausinro = int(input("Anna kuukauden numero: "))



