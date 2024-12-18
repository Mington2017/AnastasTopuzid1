f = open('24.txt')
c = 0

for i in f:
    i = i.replace('R', '1')
    i = i.replace('S', '2')
    i = i.replace('Q', '3')
    while i.count('123' * c) != 0:
        c += 1
        print(i.count('123' * c), c)