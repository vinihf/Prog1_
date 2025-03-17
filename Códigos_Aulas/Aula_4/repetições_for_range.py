'''
A repetição com a palavra reservada for é indicada
quando sabe-se o número de repetições que serão executadas.

Por exemplo:
 - Uma contagem regressiva
 - Número determinado de valores solicitados
 - Construção de um somatório

A instrução for percorre os valores dispostos em uma lista
ou string.

Para gerar as listas, utilizamos a função range. 
https://docs.python.org/3/library/functions.html#func-range

A função range recebe 3 parâmetros:
start (0 padrão)
stop (até aqui)
step (1 se padrão)
'''
for i in range(0,10,2):
    print(i)

for letra in "Programação":
    print(letra)

'''
Calcule a soma de 3 números informados por uma pessoa:
'''
soma = 0 
for i in range(3):
    soma+= int(input(f"Informe o {i} valor:"))
print(f'A soma é: {soma}')