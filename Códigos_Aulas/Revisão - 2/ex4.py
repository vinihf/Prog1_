from random import randint

def main():
    lista = []
    menor = []
    maior = []
    for i in range(100):
        lista.append(randint(1,1000))
    total = sum(lista)
    media = total/len(lista)
    for elemento in lista:
        if elemento >media:
            maior.append(elemento)
        elif elemento<media:
            menor.append(elemento)
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")
    if len(maior)>len(menor):
        print(f"Maior tem mais elementos ({len(maior)})")
    else:
        print(f"Menor tem mais elementos ({len(menor)})")

if __name__ == "__main__":
    main()