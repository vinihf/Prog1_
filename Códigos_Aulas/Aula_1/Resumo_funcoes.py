'''

    Agora iremos começar a definir nossas próprias funções. Para isso, vamos criar uma função que calcula
    o preço a ser pago na compra de sorvetes.

    Observe que o parâmetro, que é a variável que iremos precisar na função, na segunda função
    já possui um valor atribuído. A isso damos o nome de parâmetro default. Significa que
    se não informarmos um valor para ele será 0.

'''

def calcula_preco(quantidade):
    preco = quantidade * 5.5
    print(f'O valor a ser pago pelos sorvetes é de R${preco:3.2f}')

def calcula_preco_com_retorno(quantidade = 1):
    preco = quantidade * 5.5
    return preco

''' A primeira função, sem retorno, imprime diretamente o conteúdo do programa. '''
calcula_preco(4)

''' Mas, e se quisermos utilizar o valor processar e imprimir de outra forma?'''
preco = calcula_preco_com_retorno(quantidade = 4)
print(f'O valor a ser pago pelos sorvetes é de R${preco:3.2f}')

preco = calcula_preco_com_retorno()
print(f'O valor a ser pago pelos sorvetes é de R${preco:3.2f}')