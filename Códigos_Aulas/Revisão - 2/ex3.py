def isograma(palavra:str)->bool:
    letras = []
    for letra in palavra.lower():
        if letra in letras:
            return False
        else:
            letras.append(letra)
    return True

def main():
    print(isograma("machine"))
    print(isograma("isogram"))
    print(isograma("palavra"))

if __name__ == '__main__':
    main()