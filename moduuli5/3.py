
on = "On alkuluku"
ei = "Ei ole alkuluku"

while True:
    userInput = int(input("Anna luku: "))
    for i in range(2, userInput):

        if userInput % i == 0:
            print(ei)
            break
    else:
        if userInput < 2:
            print(ei)
        else:
            print(on)








