t_n = input("vnesi število")
while True:
    s_n = input("vnesi število")

    if s_n != 0 :
        if s_n < t_n:
            t_n = s_n
    elif s_n == 0:
        break



print(t_n)


