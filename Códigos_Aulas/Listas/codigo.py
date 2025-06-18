preços = []
while True:
    valor = float(input("Informe valor:"))
    if valor<0:
        break
    preços.append(valor)
soma = 0
for indice in range(0,len(preços)):
    soma += preços[indice]
print(soma)
print(sum(preços))