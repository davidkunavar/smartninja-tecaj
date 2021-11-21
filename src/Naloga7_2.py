from turtle import *
import time


hideturtle()
def odste():
    for i in range(5, 0, -1):
        clear()
        write(i, font=["arial", 50, "bold"])
        time.sleep(1)
    clear()


def klik(x, y):
    global st_klikov, start

    trenutni = time.time()
    cas = trenutni - start
    if cas < 5:
        st_klikov += 1
    else:
        write(f"Vnesli ste: {st_klikov}, v petih sek")
        time.sleep(3)
        exit()

st_klikov = 0

odste()
start = time.time()
screen = Screen()
screen.onclick(klik)
screen.listen()
screen.mainloop()