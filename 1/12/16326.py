def DEL(x, a):
    return x % a == 0

for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        f = (not(DEL(x, a))) <= ((DEL(x, 14)) <= (not(DEL(x, 4))))
        if not f:
            flag = False
            break
    if flag:
        print(a)
