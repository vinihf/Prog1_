'''

https://allendowney.github.io/ThinkPython/chap01.html
https://allendowney.github.io/ThinkPython/chap02.html

Ao executar o código no terminal do Python, é obtido o resultado  imediato da operação.
Em um script mais formal é importante podermos trabalhar com os valores desta execução.

Para isso, utilizamos variáveis. As variáveis são referências para a memória e nos possibilitam
armazenar temporariamente o código executado.

Existem algumas regras para nomear uma variável:
- Não pode iniciar por número, por exemplo:  10reais
- Não pode ter espaçamento entre palavras: dez reais
- Não pode ter caracteres especiais: 10+reais

Assim, poderia ser: dezReais, dez_reais, dezreais, reais10


'''

resultadoInteiro = 1+1
resultadoFloat = 1.1+2
resultadoString = "Olá, mundo!"

'''

Python é uma linguagem de tipagem dinâmica. Isso significa que o tipo das variáveis muda conforme o valor
que elas armazenam.

'''
variavel_x = 1
print(type(variavel_x))
variavel_x = 1.0
print(type(variavel_x))
variavel_x = "1"
print(type(variavel_x))


'''
Python é uma linguagem de tipagem forte. Tipagem forte significa que o interpretador do Python avalia as expressões 
(evaluate) e não faz coerções automáticas entre tipos não compatíveis (conversões de valores).

a = 10
b = "2"
print(a+b)

'''

'''
Com a possibilidade de armazenar valores dentro de variáveis, podemos agora construir expressões.

Assim como na matemática, há uma ordem de precedência nas expressões:
- Primeiro o que está dentro de parêntesis
- Expoentes
- Multiplicação ou Divisão
- Adição ou Subtração

'''
resultado_1 = 3 / 1 + 2 * 3 ** 2

resultado_2 = 3 / (1 + 2) * 3 ** 2

print(f'{resultado_1} != {resultado_2}')


'''
Podemos utilizar funções pré-definidas pela linguagem Python. Uma delas, muito importante, é a função print. Para que ela
funcione, precisamos informar um argumento, valor ou variável.

A função print tem por objetivo exibir conteúdo na tela quando o programa é executado. A descrição da função pede:

print(*objects, sep=' ', end='\n', file=None, flush=False)

Exibe objects no fluxo de texto arquivo, separado por sep e seguido por end. sep, end, file e flush, se houver, 
devem ser fornecidos como argumentos nomeados.

Ao adicionar f ao primeiro argumento, podemos formatar a string inserindo dentro dela uma variável.

'''
print("Resultado inteiro:")
print(resultadoInteiro)

print("Resultado float:")
print(resultadoFloat)

print("Resultado string:")
print(resultadoString)

print(f'O resultado é {resultadoFloat:3.2f}')
print(f'O resultado é {resultadoFloat:10.5f}')

'''

Existem inúmeras funções na linguagem Python que podem ser utilizadas na construção de um script. Aquelas que são
instaladas com o Python são nomeadas bibliotecas nativas. Por exemplo, round e abs. Elas necessitam de um argumento para
 funcionar.

'''
valor1 = -33.4
valor2 = -33.6

print("Arredondamento com round:")
print(round(valor1))
print(round(valor2))

print("Valor absoluto com abs:")
print(abs(valor1))
print(abs(valor2))

'''

Para arredondar valores também podemos utilizar as funçõe ceil() e floor(), da biblioteca math. Para isso, precisamos
importá-la para o nosso programa.

'''
from math import ceil, floor

print(ceil(valor1))
print(floor(valor1))

'''
Ao imprimirmos valor1 após o uso de ceil, por exemplo, verifique que seu valor não foi alterado. Isso acontece porque a
função ceil, assim como floor, rand e abs, são funções que tem retorno. Ou seja, elas processam e devolvem um valor novo.
Para guardar seu valor, precisamos armazená-lo em uma variável,
'''
print(valor1)
valor1 = ceil(valor1)
print(valor1)

'''
Uma das principais funções com retorno do Python é a função input. Através dela podemos solicitar valores para quem está
usando nosso programa.

Se tentássemos calcular o preço a ser pago:

qtd_sorvetes = input("Quantos sorvetes você quer?")
preco = qtd_sorvetes*5.5
print(preco)

Obteríamos um erro. A função input retorna por padrão um valor do tipo string. Não há como multiplicar um texto por um 
float. Assim, precisamos converter esse valor para inteiro.

'''
qtd_sorvetes = int(input("Quantos sorvetes você quer?"))
preco = qtd_sorvetes*5.5
print(preco)
print(f'O preço total é de R${preco:3.2f}')