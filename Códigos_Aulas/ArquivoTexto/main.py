def main():
    with open('arquivo.txt','r',encoding='utf-8') as arquivo:
        #Lê todo conteúdo como uma string
        conteudoTodo = arquivo.readlines()
        for linguagem in conteudoTodo:
            dados = linguagem.split("#")
            print(f'{dados[0]} ({dados[1].strip("\n")})')

if __name__ == '__main__':
    main()