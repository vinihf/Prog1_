def maioridade(idade:int) -> bool:
    """
    Verifica se uma pessoa é maior de idade.

    Args:
        idade(int):Idade

    Returns:
        bool: True se é maior de idade e False se é menor de idade.
    """
    if idade >= 18:
        return True
    else:
        return False


def main():
    nome = input("Informe seu nome:")
    idade = int(input("Informe sua idade:"))
    if maioridade(idade):
        print(f'{nome} é maior de idade.')
    else:
        print(f'{nome} é menor de idade.')

if __name__ == '__main__':
    main()