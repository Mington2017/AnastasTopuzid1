for a in range(1000):
    flag = True
    for x in range(500):
        for y in range(500):
            f = not(not((x < 7) or (y >= 3 * x + a - 20) or (x >= 34) or (y < 121)))
            if not f:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(a)
