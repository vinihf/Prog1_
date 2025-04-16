def main():
    while True:
        valor = int(input("Informe um valor entre 100 e 999:"))
        if valor>=100 and valor<=999:
            break
    centena = valor // 100
    dezena = (valor % 100) // 10
    unidade = valor % 10
    soma = centena+dezena+unidade
    print(soma)

if __name__ == "__main__":
    main()
