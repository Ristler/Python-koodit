realUser = "python"
realPassword = "rules"

user = input("Käyttäjätunnus: ")
password = input("Salasana: ")

while user != realPassword and user != realUser:
    print("Pääsy evätty.")
    user = input("Käyttäjätunnus: ")
    password = input("Salasana: ")

else:
    print("Tervetuloa!")