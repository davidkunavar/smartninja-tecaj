import math

def faktoriranje(n):

    stevec = 1
    for i in range(1, n+1, 1):
        stevec = stevec * i

    return stevec


def sinus(x):
    vsota = 0
    num = 1

    for i in range(1, 6, 1):
        if i % 2 == 0:
            vsota = vsota - (math.pow(x, num) / faktoriranje(num))
        else:
            vsota = vsota + (math.pow(x, num) / faktoriranje(num))

        num = num + 2;


    return vsota;


a = float(input("Vnesi x:"))

b = sinus(a)

print(b)







