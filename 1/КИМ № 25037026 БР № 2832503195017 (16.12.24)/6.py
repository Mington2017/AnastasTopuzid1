from turtle import *
lt(90)
tracer(0)
k = 15
down()
for i in range(2):
    fd(5 * k)
    lt(90)
    bk(13 * k)
    lt(90)
up()
bk(10 * k)
rt(90)
fd(9 * k)
lt(90)
down()
for i in range(2):
    fd(11 * k)
    rt(90)
    fd(7 * k)
    rt(90)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, 'red')
print('187')
