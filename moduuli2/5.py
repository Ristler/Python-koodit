
leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luoti: "))

luotitoG = luoti * 13.3
naulatoG = naula * 425.6
leiviskatoG = leiviska * 8512

total = luotitoG + naulatoG + leiviskatoG

kg = int(total / 1000)
g = total % 1000
print("")

print("Massa nykymittojen mukaan:")
print(kg,f"kilogrammaa ja{g:7.2f} grammaa.")





