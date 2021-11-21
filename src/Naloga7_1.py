import time
from turtle import *
import random

#read
besede = open("besedetxt", "r")
besede = besede.readlines()

filter = []

for i in range(len(besede)):
    if len(besede[i]) >= 5:
        filter.append(besede[i])

while True:
    hideturtle()
    i = random.randint(0, len(filter) - 1)

    beseda = filter[i]
    penup()
    goto(random.randint(-500, 500), random.randint(-500, 500))
    pendown()
    clear()

    write(beseda, align= "center", font= ["arial", 50, "normal"])
    time.sleep(1)


