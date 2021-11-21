from turtle import *
import time


def lik():


    kot =  180 - (((n-2)*180)/n)
    for i in range(n):
        speed(0)
        forward(dol)
        left(kot)
n = int(input("Vnesi n"))
dol = int(input("Vnesi dolzino stranice"))
st_likov = int(input("Vnesi st likov:"))

for i in range(100):
    lik()
    left(3.6)