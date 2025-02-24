'''

Crie uma função que calcula o valor de troco a ser devolvido a partir do valor da compra e do valor pago
pela cliente

'''

def troco(valor_compra:float,valor_pago:float)->float:
    return valor_pago-valor_compra


def main():
    compra = float(input('Qual é o valor total da compra? '))
    pagamento = float(input('Qual é o valor do pagamento? '))
    valor_troco = troco(compra,pagamento)
    print(f'O troco da compra é de R${valor_troco:.2f}')

if __name__ == '__main__':
    main()