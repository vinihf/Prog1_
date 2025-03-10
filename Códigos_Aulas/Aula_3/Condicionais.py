'''
Para construir desvios condicionais a linguagem Python
nos permite utilizar 4 palavras reservadas:
if, else, elif e match.

A instrução elif nos possibilita construir condições
adicionais em um encadeamento de condicionais, ou seja,
quando há mais do que duas condições.

Considere uma verificação simples para saber se um valor
inteiro é zero, positivo ou negativo.

Criar estruturas condicionais desta forma evita comparações
desnecessárias

'''
valor = int(input("Informe um valor:"))
if valor==0:
    print("É zero")
elif valor>0:
    print("É positivo")
else:
    print("É negativo")


'''
A estrutura match também nos permite construir condicionais.
Porém, é mais indicado quando se verificam igualdades:
'''
estado = input("Qual é a sigla?")
match estado.upper():
    case "RS":
        print("Rio Grande do Sul")
    case "SC":
        print("Santa Catarina")
    case "PR":
        print("Paraná")
    case _:
        print("Sigla não corresponde a nenhum estado da região sul do Brasil")
