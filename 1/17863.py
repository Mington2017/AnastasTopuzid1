f = open('17863.txt')
c = 0

for i in f:
    a = [int(x) for x in i.split()]
    a_1_1 = [x for x in a if a.count(x) == 3]
    a_1_2 = [x for x in a if a.count(x) == 1]
    a_2_1 = sum(map(int, list(a_1_1))) ** 2
    a_2_2 = sum(map(int, list(a_1_2))) ** 2
    if len(a_1_1) == 3 and len(a_1_2) == 3:
        if a_2_1 > a_2_2:
            c += 1
print(c)