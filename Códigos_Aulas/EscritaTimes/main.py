def main():
    #Neste arquivo especificamos a codificação dos caracteres
    with open("arquivo.txt", 'w', encoding='utf-8') as arquivo:
       times = ['Grêmio','Juventude','Caxias','Internacional']
       arquivo.writelines(times)

if __name__ == '__main__':
    main()