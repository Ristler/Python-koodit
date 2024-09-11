
def neworold (name):
    if name in nimet:
        print("Aiemmin syötetty nimi")
    elif name not in nimet:
        print("Uusi nimi")
    return

nimet = {""}
userInput = input("Anna nimi: ")
neworold(userInput)

while userInput != "":
    nimet.add(userInput)
    userInput = input("Anna nimi: ")
    neworold(userInput)

for i in nimet:
    print(i)
    print("----")


