besedilo = input("Vnesi besedilo")

vsota = 0

for i in range(0, len(besedilo), 1):
    if "a" <= besedilo[i] <= "z" or "A" <= besedilo[i] <= "Z" :
        vsota = vsota + 1


print(vsota)