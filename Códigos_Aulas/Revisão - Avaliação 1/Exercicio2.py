def main():
    #Iniciamos a variável x com -1 para que seja possível realizar a validação de entrada
    x = -1
    #Enquanto o valor não estiver correto será solicitado um novo valor
    while x<1 or x>10:
        x = int(input("Informe "))
    #De 0 até 10
    for v in range(0,11):
        print(f'{x} * {v} = {x*v}')

if __name__ == "__main__":
    main()