vsota = 0
delj= 0
while True:

    st = float(input("Vnesi število"))
    if st != 0:
        vsota = vsota + st
        delj+=1

    else:
        break

povprečje = vsota/delj

print(povprečje)