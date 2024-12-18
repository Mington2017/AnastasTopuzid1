a = input()

def f2(x):
    f2 = eval(a)
    return f2

for i in range(-1000, 1000):
    i = float(i / 2)
    if f2(i) == True:
        print(i)