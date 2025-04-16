def main():
    while True:
        senha = input("Informe a senha:")
        if senha == "admin123":
            print("Acesso permitido")
            break
        else:
            print("Acesso não permitido")

if __name__ == "__main__":
    main()
