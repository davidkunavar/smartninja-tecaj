from turtle import *
import time
import random



def kvadrat():
    pensize(10)
    for i in range(4):
        forward(100)
        left(90)
c

def nakljucno_skakanje():

    while True:
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        alpha = random.randint(0, 360)
        setheading(alpha)
        goto(x, y)

def nakljucno_premikanje():
    while True:
        alpha = random.randint(0, 360)
        dol = random.randint(0, 100)
        setheading(alpha)
        forward(dol)

def mravlje():

    zelvic = []
    for i in range(10):
        t = Turtle
        t.speed(0)
        zelvic.append(t)
    while True:
        for i in range(len(zelvic)):
            zelva = zelvic[i]
            alpha = random.randint(0, 360)
            dol = random.randint(0, 100)
            zelva.setheading(alpha)
            zelva.forward(dol)
def sonce():
    speed(0)
    for i in range(100):
        circle(100)
        left(3.6)
        time.sleep(5)


def oi_krogi():
    speed(0)
    for i in range(4):
        x = 125*i - 200
        y = 0
        penup()
        goto(x, y)
        pendown()
        circle(100)

    for i in range(3):
        x = 125 * i - 135
        y = -125
        penup()
        goto(x, y)
        pendown()
        circle(100)


def pobarvan_lik():
    fillcolor("red")
    circle(100)
    time.sleep(5)

def risanje_texta():
    hideturtle()
    write("Začni po odštevanju...", align= "center",  font= ["arial", 50, "normal"] )

    for i in range(10, 0, -1):
        x = i*-80 + 400
        y = -200
        penup()
        goto(x, y)
        pendown()
        write(i, align= "center", font= ["arial", 50, "normal"])
        time.sleep(1)

    penup()
    goto(0, -300)
    pendown()
    write("Start", align= "center", font= ["arial", 50, "normal"])


def ko_se_klikne(x, y):
    goto(x, y)
    r = random.randint(0, 255)/255
    g = random.randint(0, 255)/255
    b = random.randint(0, 255)/255
    dot(50, [r, g, b])

def gor():
    setheading(90)
    forward(40)
def dol():
    setheading(-90)
    forward(40)
def levo():
    setheading(180)
    forward(40)
def desno():
    setheading(0)
    forward(40)


screen = Screen()

screen.bgpic("3683.png")
screen.screensize(400, 500)
time.sleep(5)
screen.onclick(ko_se_klikne)
screen.onkeypress(gor, "Up")
screen.onkeypress(dol, "Down")
screen.onkeypress(levo, "Left")
screen.onkeypress(desno, "Right")
screen.listen()
screen.mainloop()
