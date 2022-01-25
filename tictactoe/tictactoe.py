columns = [0, 1, 2]
count = 0
plik_gry = 0
import itertools
import secrets
import os
import sys
from contextlib import redirect_stdout

def ktos_wygral():
    game_won = True
    again = input("Koniec gry, chcesz zagrac jeszcze raz? (y/n) ")
    if again.lower() == "y":
        print("restartowanie!")
        game_won = False
        os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)
    elif again.lower() == "n":
        print("Papa!")
        play = False
        plik_gry.close()
    else:
        print("Brak dobrej odpowiedzi, ale... cya!")
        play = False
        plik_gry.close()

def nikt_wygral():
    again = input("Nikt nie wygał! Chcesz zagrać jeszcze raz? (y/n) ")
    if again.lower() == "y":
        print("restartowanie!")
        game_won = False
        os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)
    elif again.lower() == "n":
        print("Papa!")
        play = False
        plik_gry.close()
    else:
        print("Brak dobrej odpowiedzi, ale... cya!")
        play = False
        plik_gry.close()

def plansza_gry(gra, player=0, line=0, column=0, just_display=False):
    try:
        if plansza[line][column] != 0:
            print("To miejsce jest zajete!")
            return False
        print("   0  1  2")
        if not just_display:
            gra[line][column] = player
        for count, line in enumerate(plansza):
            print(count, line)
        return gra
    except IndexError:
        print("Czy wlasnie probowales postawic w zlym miejscu znak?")
        return False
    except Exception as e:
        print(str(e))
        return False

def wygrana(aktualna_gra):
    #horizontal
    for line in plansza:
        if line.count(line[0]) == len(line) and line[0] != 0:
            print(f"Gracz {line[0]} wygral poziomo!")
            return True
    #vertical
    for col in range(len(plansza[0])):
        check = []
        for line in plansza:
            check.append(line[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"Gracz {check[0]} wygral pionowo!")
            return True
    # / diagonal
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(plansza)))):
        diags.append(plansza[idx][reverse_idx])

    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Gracz {diags[0]} wygral na ukos (/)")
        return True

    # \ diagonal
    diags = []
    for ix in range(len(plansza)):
        diags.append(plansza[ix][ix])

    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Gracz {diags[0]} wygral na ukos (\\)")
        return True

    return False

play = True
players = [1, 2]
while play:
    plansza = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]
    gra_koniec = False
    player_cycle = itertools.cycle([1, 2])
    plansza_gry(plansza, just_display=True)
    nazwa = input("Nazwij tą grę: ")
    plik_gry = open(nazwa + '.txt', "x")
    game_mode = int(input("Masz znajomych, czy chcesz zagrac z botem? 1 - z botem, 2 - ze znajomym: "))
    if(game_mode == 2):
        while not gra_koniec:
            current_player = next(player_cycle)
            print(f"Gracz: {current_player}")
            column_choice = int(input("Ktora kolumna? "))
            line_choice = int(input("Ktory rzad? "))
            played = plansza_gry(plansza, player=current_player, line=line_choice, column=column_choice)
            count+=1

            if wygrana(plansza):
                ktos_wygral()
            elif count == 9:
                nikt_wygral()

    elif(game_mode == 1):
        while not gra_koniec:
            current_player = next(player_cycle)
            print(f"Gracz: {current_player}")
            if current_player == 1:
                column_choice = int(input("Ktora kolumna? "))
                line_choice = int(input("Ktory rzad? "))
                played = plansza_gry(plansza, player=current_player, line=line_choice, column=column_choice)
                count+=1
            elif current_player == 2:
                inne_pole = False
                while inne_pole == False:
                    column_choice = int(secrets.choice(columns))
                    line_choice = int(secrets.choice(columns))
                    if plansza[line_choice][column_choice] == 0:
                        inne_pole = True
                played = plansza_gry(plansza, player=current_player, line=line_choice, column=column_choice)
                count+=1

            if wygrana(plansza):
                ktos_wygral()
            elif count == 9:
                nikt_wygral()

    else:
        print("Musisz kogos wybrac do gry.")
        play = False
