def main():
    with open("lista.txt","r",encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        soma = 0
        for linha in linhas:
            compra = linha.split("$")
            soma+=float(compra[1])
        print(f'${soma:.2f}')

if __name__=='__main__':
    main()