i = 0
for a in range(1, 500):
    a = bin(a)[2:]
    if a.count('1') == 8:
        i += 1
print(i)
