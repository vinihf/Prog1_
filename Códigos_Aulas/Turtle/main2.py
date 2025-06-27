import turtle


def quadradoPreenchido():
    t.pencolor("blue")
    t.pensize(3)
    t.fillcolor("yellow")
    t.begin_fill()
    for _ in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()

def circuloPreenchido(raio):
    t.pencolor("pink")
    t.pensize(3)
    t.fillcolor("black")
    t.begin_fill()
    t.circle(raio)
    t.end_fill()

def muitosCirculos(qtd):
    t.pencolor("blue")
    t.pensize(2)
    t.penup()
    t.goto(-250,135)
    t.pendown()
    tamanho = 15
    for i in range(qtd):
        t.circle(tamanho)
        t.penup()
        t.goto(-250+(i*tamanho),135-(i*tamanho))
        t.pendown()

def estrela5Pontas():
    for i in range(5):
        t.forward(150)
        t.right(144)

def flor6Petalas():
    for i in range(6):
        t.circle(50)
        t.right(60)

def rosto():
    t.speed(0)

    # Cabeça
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.fillcolor("peachpuff")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    # Olhos
    for x in [-35, 35]:
        t.penup()
        t.goto(x, 20)
        t.pendown()
        t.fillcolor("white")
        t.begin_fill()
        t.circle(15)
        t.end_fill()

    # Boca
    t.penup()
    t.goto(-30, -40)
    t.setheading(-60)
    t.width(5)
    t.pencolor("red")
    t.pendown()
    t.circle(40, 120)

    t.hideturtle()

t = turtle.Turtle()
# Podemos definir um tamanho de tela
#tela = turtle.Screen()
#tela.setup(600,400)
#print(tela.window_height())
#print(tela.window_width())
rosto()
turtle.done()