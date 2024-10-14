"""

Da mesma forma que podemos usar o padrão Docstrings para documentar as funções que escrevemos
há um padrão para realizar testes das nossas funções, o padrão doctests

https://docs.python.org/3/library/doctest.html
"""

def somar(valor1:int, valor2:int) -> int:
    """
    Calcula a soma de dois valores
    Args:
        valor1: primeiro valor(int)
        valor2: segundo valor(int)

    Returns: soma dos dois valores(int)

    >>> somar(2,4)
    6
    >>> somar(2,2)
    3
    """
    return valor1 + valor2

def main():
    print(somar(2,4))

if __name__ == '__main__':
    main()