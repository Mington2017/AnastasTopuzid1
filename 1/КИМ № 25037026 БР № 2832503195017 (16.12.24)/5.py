a = []
for n in range(1, 10000):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = b + b[-2:]
    else:
        b = '1' + b + '0'
    R = int(b, 2)
    if R < 100:
        a.append(n)
print(max(a))