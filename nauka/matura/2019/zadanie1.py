import math

with open('liczby.txt', 'r') as f:
    lines = f.read().splitlines()
count = 0
for line in lines:
    inter = int(line)
    logar = round(math.log(inter, 3), 6)
    if logar.is_integer():
        count += 1

print("Ilosc poteg liczby 3 wynosi: " + str(count))
