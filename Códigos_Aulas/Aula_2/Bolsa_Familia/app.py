def bolsaFamilia(renda:float,pessoas:int, cad_unico:str) -> bool:
    """
    Verifica se uma família pode receber o Bolsa Família

    Args:
        renda(float):Renda total da família
        pessoas(int):Total de componentes da família
        cad_unico(string):Se está cadastrada no Cadastro Único

    Returns:
        bool: True se receberá o Bolsa Família e False em caso contrário.
    """
    if ((renda/pessoas) < 218) and cad_unico == "S":
        return True
    else:
        return False


def main():
    renda_total = float(input("Informe a renda da família:"))
    pessoas_familia = int(input("Informe quantas pessoas constituem a família:"))
    cadastro_unico = input("Família no Cadastro Único? (S)im ou (N)ão")
    if (bolsaFamilia(renda_total,pessoas_familia,cadastro_unico)):
        print("Aprovado")
    else:
        print("Reprovado")

if __name__ == '__main__':
    main()