def main():
    #Preço de cada produto
    precos = {"Banana":3.80,"Maçã":4.00,"Melancia": 10.00}
    #Quantidade comprada de cada produto
    quantidade_compras = {"Banana":2,"Maçã":2,"Melancia": 1}
    soma = 0
    for chave in quantidade_compras.keys():
        soma+=precos[chave]*quantidade_compras[chave]
    print(f'R${soma:.2f}')

if __name__ == '__main__':
    main()