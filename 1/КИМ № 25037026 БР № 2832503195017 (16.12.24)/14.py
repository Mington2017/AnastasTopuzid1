def f(n):
    a = []
    while n != 0:
        a.append(n % 9)
        n = n // 9
    return a[::-1]

b = 2 * 729 ** 333 + 2 * 243 ** 334 - 81 ** 335 + 2 * 27 ** 336 - 2 * 9 ** 337 - 338
c = f(b)
c = len(c) - c.count(0)
print(c)