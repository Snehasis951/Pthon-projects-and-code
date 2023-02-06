import turtle as t 
import colorsys

t.bgcolor('black')
t.speed('fastest')
t.tracer(100)
t.pencolor('blue')
hue = 0.7
t.hideturtle()

def VastCoding():
    global hue
    for i in range(4):
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        hue += 0.004
        t.fillcolor(color)
        t.begin_fill()
        t.fd(100)
        t.right(50)
        t.fd(100)
        t.end_fill()

for j in range(400):
    VastCoding()
    t.goto(0,0)
    t.rt(0)

t.exitonclick() 

