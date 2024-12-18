a = input()

def f(x):
    f = eval(a)
    return f

for i in range(-10, 10):
    i = float(i / 2)
    if f(i) == True:
        print(i)



