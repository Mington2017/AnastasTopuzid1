f = open("12726.txt")
c = 0

for i in f:
    a = [int(x) for x in i.split()]
    a_11 = [x for x in a if a.count(x) == 3]
    a_12 = [x for x in a if a.count(x) == 1]
    a_21 = [x for x in a if x % 2 == 0]
    a_22 = [x for x in a if x % 2 != 0]
    c += 1
    if len(a_11) == 3 and len(a_12) == 4:
        if len(a_21) > len(a_22):
            print(c)
