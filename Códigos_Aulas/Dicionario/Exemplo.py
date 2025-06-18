def main():
    dados = {}
    while True:
        nome = input("Informe um nome:")
        idade = int(input("Informe a idade da pessoa"))
        dados[nome] = idade
        continuar = input("Quer continuar? (S)im ou (N)ão ")
        if continuar == "N":
            break
    for chave,valor in dados.items():
        print(f'{chave} - {valor}')

if __name__ == "__main__":
    main()