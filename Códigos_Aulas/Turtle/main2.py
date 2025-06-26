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
    

t = turtle.Turtle()

# Podemos definir um tamanho de tela
tela = turtle.Screen()
tela.setup(600,400)
#print(tela.window_height())
#print(tela.window_width())
muitosCirculos(5)
turtle.done()