def main():
    texto = "Deixe-me começar dizendo o que pensamento computacional não é. Não se trata, por exemplo, de saber navegar na internet, enviar email, publicar um blog, ou operar um processador de texto. Pensamento computacional é saber usar o computador como um instrumento de aumento do poder cognitivo e operacional humano – em outras palavras, usar computadores, e redes de computadores, para aumentar nossa produtividade, inventividade, e criatividade. Grandes intelectuais da educação, como Seymour Papert e Andrea diSessa, já publicaram vários livros sobre o assunto. Estamos em uma época de transição no mundo científico, em que o pensamento computacional está transformando profundamente a academia e a indústria. Hoje em dia, um cientista em um laboratório de pesquisa de ponta em nada lembra o estereótipo do cientista do século XIX, com seu avental branco, trancado em um laboratório com tubos de ensaio. Em vez disso, ele provavelmente passa a maior parte do tempo em frente a um computador, construindo e estudando modelos computacionais. Um engenheiro industrial, ao tentar redesenhar a linha de produção, não usa só papel e lápis – usa modelos computacionais. Um economista tentando fazer uma projeção de inflação não faz as contas de cabeça – usa, claro, modelos. A primeira etapa do pensar computacionalmente é identificar as tarefas cognitivas que podem ser feitas de forma mais rápida e eficiente por um computador. A segunda etapa é saber programar um computador para realizar essas tarefas cognitivas em outras palavras, transferir aquilo que não é essencialmente humano para um computador que, como sabemos, é bem burrinho, mas muito rápido."
    texto_limpo = texto.replace(",","").replace(".","").lower().split(" ")
    for palavra in texto_limpo:
        #if palavra[0] == "b":
        #if palavra.startswith("b"):
        #if palavra.endswith("n"):
            print(palavra)



if __name__ == "__main__":
    main()