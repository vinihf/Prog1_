import turtle

t = turtle.Turtle()
t.pencolor("blue")
t.pensize(3)
t.fillcolor("yellow")

t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

turtle.done()