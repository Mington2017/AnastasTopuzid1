for x in range(10):
    for y in range(10):
        for z in range(10):
            for w in range(10000):
                f = '12' + str(x) + '3' + str(w) + '456' + str(y) + str(z) + '9'
                f = int(f)
                if (f <= 10 ** 12) and (f % 98591 == 0):
                    print(f, f // 98591)