import turtle

from matplotlib import colors
turtle.bgcolor('black')
turtle.speed(50)
turtle.pensize(2)
colors = ('aqua', 'red', 'ghostwhite', 'lawngreen', 'magenta', 'peachpuff')

for i in range (200):
    turtle.forward(i*4)
    turtle.right(91)
    turtle.color(colors[i%6])

    for j in range(3):
        turtle.forward(j*4)
        turtle.right(91)

        for k in range(2):
            turtle.forward(k*4)
            turtle.right(91)

            for l in range(739):
                turtle.forward(l*4)
                turtle.right(891)
