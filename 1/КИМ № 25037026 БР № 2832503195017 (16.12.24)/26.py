f = open('26.txt')
a = []
b = []
c = 0
k = 0

for i in f:
    a.append(i)

for i in a:
    if int(a[1]) * int(a[k + 2]) <= int(a[0]):
        c = (a[1]) * (a[k + 2])
        b.append(c)
        k += 1
print(b, k)



