while True:
    try:
        produto = float(input("Informe o preço do produto:"))
        pago = float(input("Informe o valor pago:"))
        troco = pago-produto
        print(f'O troco é de R${troco:.2f}')
        break
    except ValueError:
        print("Deve ser um valor Float!!")
