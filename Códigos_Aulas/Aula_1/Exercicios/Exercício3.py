'''

A quantas milhas corresponde 10km? ( 1km = 1.6 mi)

'''


def km_mi(km:int):
    """Converte de km para mi

        Parameters:
        km (int): valor de quilômetros

        Returns:
        int:valor de milhas

       """
    return km*1.6

def main():
    km = int(input("Informe os km:"))
    mi = km_mi(km)
    print(f"{km} km corresponde a {mi} mi")

if __name__ == '__main__':
    print(km_mi.__doc__)
    main()