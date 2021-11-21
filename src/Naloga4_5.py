besedilo = input("vnesi število")

vsota = 0
for i in range(0, len(besedilo), 1):
    if "a" <= besedilo[i] <= "z" or "A" <= besedilo[i] <= "Z" :
        vsota = vsota + 1

for i in range (0, len(besedilo), 1):
    if "!" <= besedilo[i] <= "/" or ":" <= besedilo[i] <= "@":
        vsota = vsota + 1

print(vsota)