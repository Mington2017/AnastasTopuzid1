a = input()

def f1(n):
    if n.count('x ** 2') == 1 or n.count('x**2') == 1:
        return 2
    else:
        return 1

def f2(x):
    f2 = eval(a)
    return f2

if f1(a) == 1:
    for i in range(-500, 500):
        i = float(i / 2)
        if f2(i) == True:
            if i % 10 == 0:
                print(int(i // 10))
            else:
                print(i)
elif f1(a) == 2:
    for i in range(-500, 500):
        i = float(i / 2)
        if f2(i) == True:
            if i % 10 == 0:
                print(int(i // 10))
            else:
                print(i)



