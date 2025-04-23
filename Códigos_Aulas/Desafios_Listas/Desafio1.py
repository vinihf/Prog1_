def main():
    texto = 'Deixe-me começar dizendo o que pensamento computacional não é. Não se trata, por exemplo, de saber navegar na internet, enviar email, publicar um blog, ou operar um processador de texto. Pensamento computacional é saber usar o computador como um instrumento de aumento do poder cognitivo e operacional humano – em outras palavras, usar computadores, e redes de computadores, para aumentar nossa produtividade, inventividade, e criatividade. Grandes intelectuais da educação, como Seymour Papert e Andrea diSessa, já publicaram vários livros sobre o assunto. Estamos em uma época de transição no mundo científico, em que o pensamento computacional está transformando profundamente a academia e a indústria. Hoje em dia, um cientista em um laboratório de pesquisa de ponta em nada lembra o estereótipo do cientista do século XIX, com seu avental branco, trancado em um laboratório com tubos de ensaio. Em vez disso, ele provavelmente passa a maior parte do tempo em frente a um computador, construindo e estudando modelos computacionais. Um engenheiro industrial, ao tentar redesenhar a linha de produção, não usa só papel e lápis – usa modelos computacionais. Um economista tentando fazer uma projeção de inflação não faz as contas de cabeça – usa, claro, modelos. A primeira etapa do pensar computacionalmente é identificar as tarefas cognitivas que podem ser feitas de forma mais rápida e eficiente por um computador. A segunda etapa é saber programar um computador para realizar essas tarefas cognitivas – em outras palavras, transferir aquilo que não é essencialmente humano para um computador que, como sabemos, é bem burrinho, mas muito rápido.'
    texto_limpo = texto.replace(",","").replace(".","").lower().split(" ")
    #Palavras com vogais
    comA = 0
    comE = 0
    comI = 0
    comO = 0
    comU = 0
    computador = 0
    iniciaFinalizaVogal = 0
    tamanho = -1
    maiorPalavra = ''

    for palavra in texto_limpo:
        if palavra.startswith("a"):
            comA+=1
        elif palavra.startswith("e") or palavra.startswith("é"):
            comE+=1
        elif palavra.startswith("i"):
            comI+=1
        elif palavra.startswith("o"):
            comO+=1
        elif palavra.startswith("u"):
            comU+=1
        elif palavra == "computador":
            computador+=1

        if palavra[0] in "aeiou" and palavra[-1] in "aeiou":
            iniciaFinalizaVogal += 1
            print(palavra)

        if len(palavra) > tamanho:
            tamanho = len(palavra)
            maiorPalavra = palavra

    print(f'{comA} iniciam com A')
    print(f'{comE} iniciam com E')
    print(f'{comI} iniciam com I')
    print(f'{comO} iniciam com O')
    print(f'{comU} iniciam com U')
    print(f'{computador} vezes aparece a palavra Computador')
    print(f'{iniciaFinalizaVogal} palavras iniciam e finalizam com vogal')
    print(f'{maiorPalavra} é a maior palavra e tem {tamanho} caracteres')

if __name__ == "__main__":
    main()