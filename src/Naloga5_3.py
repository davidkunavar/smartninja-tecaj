beseda = input("Vnesi skrito besedo:")

prazno = []
poizkus = len(beseda)*3

for i in beseda:
    prazno.append("_")

for i in range(len(beseda)*3):
    crka = input(f"Vnesi crka {poizkus} poizkiso: ")
    poizkus -= 1
    for j in range(len(beseda)):
        if crka == beseda[j]:
            prazno[j] = crka


    print("".join(prazno))

    if "_" not in prazno:
        print("Zmagal si")
        break










2






































