sukupuoli = input("Biologinen sukupuoli: ")
hemoglb = float(input("Hemoglobiiniarvo: "))

if sukupuoli == "nainen" and 175 >= hemoglb >= 117:
    print("Normaali")
elif sukupuoli == "nainen" and hemoglb < 117:
    print("Alhainen.")
    print("---------")
    print("Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.")

if sukupuoli == "mies" and 134 <= hemoglb <= 195:
    print("Normaali")
elif sukupuoli == "mies" and hemoglb < 134:
    print("Alhainen.")
    print("---------")
    print("Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.")



