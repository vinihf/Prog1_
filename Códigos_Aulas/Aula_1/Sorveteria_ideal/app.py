from Sorveteria import calcula_preco_com_retorno

def main():
    qtd = int(input("Informe a quantidade de sorvetes comprados:"))
    preco = calcula_preco_com_retorno(quantidade = qtd)
    print(f'Preço total: R${preco:3.2f}')
    print(calcula_preco_com_retorno.__doc__)

if __name__ == '__main__':
    main()