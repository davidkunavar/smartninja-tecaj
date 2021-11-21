besedilo = input("VNesi besedilo")
stevec = 0
for i in range(0, len(besedilo), 1):
    if besedilo[i] == ".":
        stevec += 1

print(f"Št povedei je: {stevec}")