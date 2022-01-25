plansza = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

def plansza_gry(gra, player=0, line=0, column=0, just_display=False):
    print("   0  1  2")
    if not just_display:
        gra[int(line)][int(column)] = int(player)
    for count, line in enumerate(plansza):
        print(count, line)
    return gra

plik_nazwa = input("Podaj nazwę pliku (wraz z rozszerzeniem): ")

with open(plik_nazwa, 'r') as plik:
    plansza_gry(plansza, just_display=True)
    rows = plik.readlines()
    for row in rows:
        if row[0] == '3':
            print("Wygrał gracz " + row[2])
        elif row[0] == '1' or row[0] == '2':
            current_player = row[0]
            line_choice = row[2]
            column_choice = row[4]
            plansza_gry(plansza, player=current_player, line=line_choice, column=column_choice)
        
