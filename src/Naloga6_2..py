import random
from getpass import getpass
s = 1
p = 2
k = 3

vsotaC = 0
vsotaU = 0

while True:

    comp = int(getpass("drugi igralec vnesi"))
    user = int(input("Vnesi stevilko med 1 in 3 (skarje = 1, papir = 2, kamen = 3:"))
    #skarje
    if comp == s and user == p:
        vsotaC += 1
    elif comp == s and user == k:
        vsotaU += 1
    elif comp == p and user == k:
        vsotaU += 1
    elif user == s and comp == p:
        vsotaU += 1
    elif user == s and comp == k:
        vsotaC += 1
    elif user== p and comp == k:
        vsotaU += 1
    print(f"Igralec: {vsotaU}", f"Računalnik: {vsotaC}")

    if vsotaU == 5 or vsotaC == 5:
        break
if vsotaU > vsotaC:
    print("Zmagal je igralec")

















