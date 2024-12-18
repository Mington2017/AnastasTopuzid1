f = open('17968.txt')
c = 0

for i in f:
    a = [int(x) for x in i.split()]
    a_1_1 = max(x)
    a_1_2 = [sum(map(int, list(str(x)))) for x in a]
    a_2_1 = [sum(map(int, list(str(x)))) for x in a if x % 2 == 0]
    a_2_2 = [sum(map(int, list(str(x)))) for x in a if x % 2 != 0]
    if a_1_1 < a_1_2:
        if a_2_1 == a_2_2:
            c += 1
print(c)