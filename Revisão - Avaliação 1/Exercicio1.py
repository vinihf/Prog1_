'''
A função parImpar estabelece que os dois valores enviados por parâmetro devem ser inteiros.
Além disso, indica também que o retorno da função deve ser do tipo bool (True ou False)
'''
def parImpar(val1:int,val2:int)->bool:
    if (val1+val2)%2==0:
        return True
    else:
        return False
    
'''
    É na função main() que são solicitados os valores e chamada a função definida anteriormente.
'''
def main():
    v1 = int(input("Valor 1:"))
    v2 = int(input("Valor 2:"))
    print(parImpar(v1,v2))

if __name__ == "__main__":
    main()