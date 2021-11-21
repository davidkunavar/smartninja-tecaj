import turtle

n = int(input("Vnesi stevilo kotov:"))
x = int(input("Vensi dolzino dtranice"))

kot = 180 - (((n-2)*180)/n)

for i in range(n):
    turtle.forward(x)
    turtle.speed(1)
    turtle.left(kot)
