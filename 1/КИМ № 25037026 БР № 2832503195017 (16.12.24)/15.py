for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        f = (x & a == 0) or (not(x & 37 == 0)) or (not(x & 12 == 0))
        if not f:
            flag = False
            break
    if flag:
        print(a)