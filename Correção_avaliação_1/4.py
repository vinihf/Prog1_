def main():
    senha_correta = "admin123"
    while True:
        senha = input("Informe a senha:")
        if senha == senha_correta:
            print("Acesso permitido")
            break
        else:
            print("Acesso não permitido")

if __name__ == "__main__":
    main()
