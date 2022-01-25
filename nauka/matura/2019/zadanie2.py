def silnia(n): #definiuje silnia dla n, czyli pojedynczej cyfry z kazdej liczby
    if n == 0: #jesli cyfra wynosi zero stopujemy
        return 1
    return silnia(n-1)*n


with open('liczby.txt', 'r') as f:
    lines = f.read().splitlines()

for line in lines: #dla kazdej linijki w liniach
    if len(line) == 0: #jesli dlugosc wynosi zero to pomijamy linie
        continue
    liczba = int(line)
    suma = 0
    for char in line: #dla kazdego znaku w linii
        n = int(char) #zmieniamy znak na cyfre
        suma += silnia(n) #sumujemy def
    if suma == liczba: #jesli suma silni wynosi liczbe wypisz
        print(liczba)