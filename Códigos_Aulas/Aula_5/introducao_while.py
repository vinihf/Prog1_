'''
A estrutura de repetição while tem por objetivo construir loops condicionais.
Ou seja, enquanto alguma condição é satisfeita, a ação é executada.

No exemplo abaixo, usamos a estratégia de uma varíavel para contagem.
A cada execução do loop a variável é decrementada.
'''
contador = 5
soma = 0
while contador>0:
    valor = int(input("Informe um valor:"))
    soma+=valor
    #Aqui decrementamos em um a variável
    contador-=1
print(f'A soma total é de {soma}')

'''
O uso do while para executar repetições é aceito. Todavia, esta estrutura
é mais útil para quando não se sabe o número total de repetições.

Vamos supor um programa que solicita valores até que a pessoa digite -1.
'''
continua = True
soma = 0
while continua:
    valor = int(input("Informe um valor:"))
    if valor!=-1:
        soma+=valor
    else:
        continua = False
print(f'A soma total é de {soma}')    

'''
Uma forma mais simples para construirmos o mesmo programa necessita
da instrução break. Ao ser utilizada, ela interrompe o laço em que está inserida.
'''
soma = 0
while True:
    valor = int(input("Informe um valor:"))
    if valor==-1:
        break
    soma+=valor
print(f'A soma total é de {soma}')    

'''
Podemos também utilizar o laço while para fazer uma validação simples de dados.
Por exemplo, vamos supor que só são aceitos valores positivos em um programa:
'''
valor = -1
while valor<0:
    valor = int(input("Informe um valor positivo:"))
print(valor)