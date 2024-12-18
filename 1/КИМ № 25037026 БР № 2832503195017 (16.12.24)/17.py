a = []
f = open('17.txt')
c = 0
d = 1
e = 0

for i in f:
    a.append(i)

c = len(a)

while c != 0:
    if int(a[-1 + d]) % 10 == 3 or int(a[1 + d]) % 10 == 3 or int(a[2 + d]) % 10 == 3:
        if len(max(a)) == 5:
            if a[-1 + d] + a[1 + d] + a[2 + d] <= max(a):
                c = c - 1
                d += 1
                e += 1
print(e)


