def dobi_kordinate(polje, znak):

    x1 = int(input("Vensi x:"))
    y1 = int(input("Vnesi y:"))

    if polje[y1][x1]  == ".":
        polje[y1][x1] = znak

    elif polje[y1][x1] != ".":
        print("ponovno")

    return polje

def izris_polja(polje):
    for y in range(3):
        for x in range(3):
            print(polje[y][x], end= " ")
        print()



polje = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
]
for i in range(9):
    dobi_kordinate(polje, "x")
    izris_polja(polje)

    dobi_kordinate(polje, "o")
    izris_polja(polje)




















