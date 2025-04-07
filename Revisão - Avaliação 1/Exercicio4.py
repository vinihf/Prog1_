def main():
    notaFinal = -1
    while notaFinal<0 or notaFinal>=10:
        notaFinal = float(input("Informe a nota final do aluno"))
    #Aqui construímos os testes de intervalo
    if notaFinal<5:
        print("D")
    elif notaFinal>=5 and notaFinal<7:
        print("C")
    elif notaFinal>=7 and notaFinal<9:
        print("B")
    else:
        print("A")

if __name__ == "__main__":
    main()