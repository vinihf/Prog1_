def main():
    l1 = [1,2,3,4]
    l2 = [4,2,1,4]
    l3 = []
    soma = 0
    for indice in range(0,len(l1)):
        soma = l1[indice]+l2[indice]
        l3.append(soma)
    print(l3)

if __name__ == "__main__":
    main()