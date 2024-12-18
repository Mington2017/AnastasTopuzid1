f = open('9.txt')
c = 0
for i in f:
    a = [int(x) for x in i.split()]
    a11 = [x for x in a if a.count(x) == 2]
    a12 = [x for x in a if a.count(x) == 1]
    if len(a11) == 6 and len(a12) == 1:
        if ((min(a11) + max(a11)) // 2) < max(a12):
            c += 1
print(c)