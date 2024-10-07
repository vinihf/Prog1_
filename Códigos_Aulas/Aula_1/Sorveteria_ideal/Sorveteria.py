'''

Docstrings

https://gist.github.com/nipunsadvilkar/fec9d2a40f9c83ea7fd97be59261c400
'''

def calcula_preco_com_retorno(quantidade:int = 1, preco_unitario:float = 5.5)->float:
    """
    Função para calcular o preço da compra de sorvetes

    :param quantidade: quantidade de sorvetes
    :param preco_unitario: preço de um sorvete
    :return: preço da compra
    """
    preco = quantidade * preco_unitario
    return preco