import turtle

clr = ('yellow', 'green', 'purple', 'pink')
turtle.pensize(5)
for r in range(4):
    turtle.rt(90)
    size=100
    for n in clr:
        turtle.color('black', n)
        turtle.begin_fill()
        for j in range(4):
            turtle.fd(size)
            turtle.rt(90)
        turtle.end_fill()
        size=size-20
