besedilo = input("Vnesi besedilo:")

vsota = 0
for i in range (0, len(besedilo), 1):
    if "!" <= besedilo[i] <= "/" or ":" <= besedilo[i] <= "@":
        vsota = vsota + 1

print(vsota)