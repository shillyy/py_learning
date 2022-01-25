strings = []
sequence = []
temps = ""
prev_letter = ""
path = "D:\Moje Tajne Rzeczy\jebac szkole\cpp python\matura20\Dane_PR2\pary.txt"

with open(path, 'r') as f:
    lines = f.readlines()

for line in lines:    # czytanie tylko wyrazow
    string = line.replace(" ", "")
    strings.append(string[2:])

for line in strings:    # tworzenie tabeli z identycznymi znakami
    for letter in line:
        prev_letter = letter
        if letter == prev_letter:
            temps += letter
    sequence.append(temps)
    prev_letter = ""
    temps = ""

for line in sequence:
    print(line)
