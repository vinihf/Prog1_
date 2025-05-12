from random import randint

lados = {}
for x in range(0,100000000000000):
    lado = randint(1,6)
    lados[lado] = lados.get(lado,0)+1
print(lados)