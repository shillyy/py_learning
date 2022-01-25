count = 100
n = 0 #liczba F(n)
n1, n2 = 0, 1 #potrzebne do obliczenia ciagu, kolejno F(n-1), F(n-2)
while n<count:
    print(n1)
    nth = n1 + n2 #nth: F(n)
    n1 = n2
    n2 = nth
    n+=1