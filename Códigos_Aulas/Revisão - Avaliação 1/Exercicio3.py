def fatorial(valor:int)->int:
    #Fatorial de 1 ou 0 é 1
    if valor==1 or valor==0:
        return 1
    else:
        #Cria um variável para acumular o valor da multiplicação
        acumulador = 1
        #De forma descrescente multiplica do valor até 1
        for x in range(valor,0,-1):
            acumulador*=x
        return acumulador

def main():
    valor = -1
    while valor <0:
        valor = int(input("Informe um valor inteiro positivo para calcular o fatorial:"))
    print(fatorial(valor))

if __name__ == "__main__":
    main()