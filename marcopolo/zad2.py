#ja pierdoleXD
import math

nr = 2 #numer z dziennika
rez = nr ** 4
puls = nr * 10
faza = 0

#moge juz skonczyc
nap_max = int(input("Podaj napiecie maksymalne w jednostkach: "))
napiecie_przemienne_sin = nap_max * math.sin(puls + faza)
napiecie_skuteczne = 1
napiecie_srednie = 2/math.pi * nap_max
natezenie_pradu = 1

print("Napięcie przemienne sinusoidalne: u = " + str(nap_max) + "*sin(" + str(puls) + "*" + str(faza) + ") = " + str(napiecie_przemienne_sin)) 
#PROSZĘ KURWA MAM DOŚĆ
print("Napięcie skuteczne: ")
print("Napięcie  średnie: 2/(pi)*" + str(nap_max) +" = " + str(napiecie_srednie))
print("Natężenie prądu: ")
#poddałam się, połowa jest źle, te wzroy to chuj, jak uda Ci się dostać od niego wzory to na podstawie tego może coś napiszesz