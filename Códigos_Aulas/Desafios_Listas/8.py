def main():
    l1 = [1,2,3,4]
    l2 = [4,2,1,4]
    contador = 0
    for indice in range(0,len(l1)):
        if l1[indice] == l2[indice]:
            contador+=1
    print(contador)


if __name__ == "__main__":
    main()