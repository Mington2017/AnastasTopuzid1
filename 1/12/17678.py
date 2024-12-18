for a in range(1000):
    flag = True
    for x in range(1, 500):
        for y in range(1, 500):
            f = (x + y <= 24) or (y <= x - 2) or (y >= a)
            if not f:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(a)