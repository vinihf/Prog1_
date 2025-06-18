def temLinguagem(lang:str)->bool:
    with open('arquivo.txt','r',encoding='utf-8') as arquivo:
        #Lê todo conteúdo como uma string
        conteudoTodo = arquivo.readlines()
        for linguagem in conteudoTodo:
            if lang == linguagem.strip("\n"):
                return True
        return False

def main():
    print(temLinguagem("Python"))
    print(temLinguagem("PHP"))

if __name__ == '__main__':
    main()