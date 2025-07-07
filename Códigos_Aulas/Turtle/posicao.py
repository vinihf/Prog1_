import turtle

t = turtle.Turtle()
t.speed(100)
for i in range(100):
    if i%2==0:
        t.fillcolor("#77b588")
    else:
        t.fillcolor("#c9a46f")
    t.begin_fill()
    t.circle(5+(i*2))
    t.end_fill()
    t.right(70)
    t.forward(i*3)
turtle.done()

