tablica = []
count = 1
x = 0
pierwsze = []
path = "D:\Moje Tajne Rzeczy\jebac szkole\cpp python\matura20\Dane_PR2\pary.txt"

for num in range(0, 100):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            if num % 2 != 0:
                pierwsze.append(num)

with open(path, 'r') as f:
    lines = f.readlines()

for line in lines:
    liczba = (int(line[:2]))
    if liczba % 2 == 0 and liczba > 4: 
        tablica.append(liczba)

for line in tablica:
    for dzielnik1 in pierwsze:
        x = line - dzielnik1
        for dzielnik2 in pierwsze:
            if dzielnik2 == x:
                print(str(line) + " " + str(dzielnik1) + " " + str(dzielnik2))
                break
        else:
            continue
        break