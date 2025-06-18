def main():
    with open("arquivo.txt","w") as arquivo:
        nome = input("Informe um nome:")
        arquivo.write(nome)

if __name__ == "__main__":
    main()