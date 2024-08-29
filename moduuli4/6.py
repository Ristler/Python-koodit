import random

inCircle = 0
n = int(input("Kuinka monta pistettä arvioidaan neliön sisälle?: "))

for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x * x + y * y < 1:
        inCircle += 1

print("Arvioitu π:",inCircle/n * 4)

