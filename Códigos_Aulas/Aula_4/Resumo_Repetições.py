"""
https://allendowney.github.io/ThinkPython/chap03.html

O uso de funções possui dois grandes objetivos:
1 - Agrupar funcionalidades em pequenos módulos
2 - Reaproveitar código

Vamos tentar fazer um teste com a música "Sujeito de sorte", do cantor Belchior.
https://www.youtube.com/watch?v=mGAra8tXeJc

A música é composta de um verso e um refrão, que se repetem e se intercalam.
Observe que abaixo podemos reutilizar as funções quantas vezes seja necessário
"""

def verso()->None:
    """
    Imprime  primeiro verso da música Sujeito de sorte, de Belchior

    Returns: None

    """
    print("Presentemente eu posso me considerar um sujeito de sorte")
    print("Porque apesar de muito moço, me sinto são e salvo e forte")
    print("E tenho comigo pensado, Deus é brasileiro e anda do meu lado")
    print("E assim já não posso sofrer no ano passado")

def refrao()->None:
    """
    Imprime  o refrão da música Sujeito de sorte, de Belchior

    Returns: None

    """
    print("Tenho sangrado demais, tenho chorado pra cachorro")
    print("Ano passado eu morri, mas esse ano eu não morro")
    print("Tenho sangrado demais, tenho chorado pra cachorro")
    print("Ano passado eu morri, mas esse ano eu não morro")
    print("Ano passado eu morri, mas esse ano eu não morro")
    print("Ano passado eu morri, mas esse ano eu não morro")

def main():
    '''verso()
    print("\n")
    refrao()
    print("\n")
    verso()
    print("\n")
    refrao()
    '''

    '''
    E se pudéssemos repetir um determinado número de vezes um conjunto de códigos?
    
    Para isso existem os comandos de repetição. 
    
    O primeiro que iremos estudar é o comando for.
    
    '''

    for i in range(3):
        verso()
        print("\n")
        refrao()
        print("\n")

if __name__ == '__main__':
    main()