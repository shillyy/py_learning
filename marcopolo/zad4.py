zdanie = "Ala ma kota"
literki = [0]
count = 0
for litera in zdanie:
    if litera == "a":
        literki.append(count)
    count+=1
for litera in literki:
    print(litera)
#to akurat es