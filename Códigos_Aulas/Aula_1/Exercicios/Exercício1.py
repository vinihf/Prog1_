'''

Elabore um programa que solicita para a pessoa usuária dois valores inteiros e os armazena respectivamente
nas variáveis X e Y. Após, o programa deve trocar os valores entre as variáveis e imprimir o resultado.

'''
try:
    X = int(input("Informe um valor inteiro:"))
    Y = int(input("Informe um valor inteiro:"))
    aux = X
    X = Y
    Y = aux
    print(f'{X} e {Y}')
except ValueError:
    print("Valores devem ser do tipo inteiro.")

