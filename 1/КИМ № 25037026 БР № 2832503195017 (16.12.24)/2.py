print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = y and (x or z) or (not(y or z)) or w
                if F == 0:
                    print(x, y, z, w, int(F))
print('xywz')