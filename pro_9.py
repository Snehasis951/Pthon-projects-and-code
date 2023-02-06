import turtle as tu 

ro = tu.Turtle()
wn = tu.Screen()
wn.bgcolor('black')
wn.title("Fractional Tree Pattern")
ro.left(90)
ro.speed(1000)

def draw(l):
    if (l<10):
        return
    else:
        ro.pensize(2)
        ro.pencolor("yellow")
        ro.forward(l)
        ro.left(30)
        draw(3 * l/4)
        ro.right(60)
        draw(3 * l/4)
        ro.left(30)
        ro.pensize(2)
        ro.backward(l)

draw(20)
ro.right(90)
ro.speed(5000)

def draw(l):
    if (l<10):
        return
    else:
        ro.pensize(2)
        ro.pencolor("green")
        ro.forward(l)
        ro.left(30)
        draw(3 * l/4)
        ro.right(60)
        draw(3 * l/4)
        ro.left(30)     
        ro.pensize(2)
        ro.backward(l)

draw(20)
ro.left(270)
ro.speed(5000)

def draw(l):
    if (l<10):
        return
    else:
        ro.pensize(2)
        ro.pencolor("blue")
        ro.forward(l)
        ro.left(30)
        draw(3 * l/4)
        ro.right(60)
        draw(3 * l/4)
        ro.left(30)
        ro.pensize(2)
        ro.backward(l)

draw(20)
ro.right(90)
ro.speed(5000)

def draw(l):
    if (l<10):
        return
    else:
        ro.pensize(2)
        ro.pencolor("red")
        ro.forward(l)
        ro.left(30)
        draw(3 * l/4)
        ro.right(60)
        draw(3 * l/4)
        ro.left(30)
        ro.pensize(2)
        ro.backward(l)

draw(20)

def draw(l):
    if (l<10):
        return
    else:
        ro.pensize(3)
        ro.pencolor("yellow")
        ro.forward(l)
        ro.left(30)
        draw(4 * l/5)
        ro.right(60)
        draw(4 * l/5)
        ro.left(30)
        ro.pensize(3)
        ro.backward(l)

draw(40)
ro.right(90)
ro.speed(5000)

def draw(l):
    if (l<10):
        return
    else:
        ro.pensize(3)
        ro.pencolor("green")
        ro.forward(l)
        ro.left(30)
        draw(4 * l/5)
        ro.right(60)
        draw(4 * l/5)
        ro.left(30)
        ro.pensize(3)
        ro.backward(l)

draw(40)
ro.left(270)
ro.speed(5000)

def draw(l):
    if (l<10):
        return
    else:
        ro.pensize(3)
        ro.pencolor("blue")
        ro.forward(l)
        ro.left(30)
        draw(4 * l/5)
        ro.right(60)
        draw(4 * l/5)
        ro.left(30)
        ro.pensize(3)
        ro.backward(l)

draw(40)
ro.right(90)
ro.speed(5000)

def draw(l):
    if (l<10):
        return
    else:
        ro.pensize(3)
        ro.pencolor("red")
        ro.forward(l)
        ro.left(30)
        draw(4 * l/5)
        ro.right(60)
        draw(4 * l/5)
        ro.left(30) 
        ro.pensize(3)
        ro.backward(l)

draw(40)

def draw(l):
    if (l<10):
        return
    else:
        ro.pensize(2)
        ro.pencolor("yellow")
        ro.forward(l)
        ro.left(30)
        draw(6 * l/7)
        ro.right(60)
        draw(6 * l/7)
        ro.left(30)
        ro.pensize(2)
        ro.backward(l)

draw(60)
ro.right(90)
ro.speed(5000)

def draw(l):
    if (l<10):
        return
    else:
        ro.pensize(2)
        ro.pencolor("green")
        ro.forward(l)
        ro.left(30)
        draw(6 * l/7)
        ro.right(60)
        draw(6 * l/7)
        ro.left(30)
        ro.pensize(2)
        ro.backward(l)


draw(60)
ro.left(270)
ro.speed(5000)

def draw(l):
    if (l<10):
        return
    else:
        ro.pensize(2)
        ro.pencolor("blue")
        ro.forward(l)
        ro.left(30)
        draw(6 * l/7)
        ro.right(60)
        draw(6 * l/7)
        ro.left(30)
        ro.pensize(2)
        ro.backward(l)

draw(60)
ro.right(90)
ro.speed(5000)

def draw(l):
    if (l<10):
        return
    else:
        ro.pensize(2)
        ro.pencolor("red")
        ro.forward(l)
        ro.left(30)
        draw(6 * l/7)
        ro.right(60)
        draw(6 * l/7)
        ro.left(30)
        ro.pensize(2)
        ro.backward(l)


draw(60)
wn.exitonclick()