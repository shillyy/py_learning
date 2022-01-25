from random import random
import secrets
ilosc = int(input("Podaj ilosc liczb: "))
i = 0
while(ilosc>i):
    print(secrets.randbelow(100))
    i += 1