# Importação da biblioteca pandas com o nome pd
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Fazendo a leitura de um arquivo ".csv"
    pokemons = pd.read_csv('Pokemon.csv')

    # Imprimir os cinco primeiros
    print(pokemons.head())

    # Buscar uma coluna
    # print(pokemons['Name'])

    # Armazenar os dados em formato de Serie
    nomes = pokemons['Name']
    # print(nomes)

    # Buscar mais de uma coluna
    print(pokemons[['Name','Type 1']].head())

    # Identificar o tamanho de um DataFrame
    print(pokemons[['Name','Type 1']].shape)

    # Para selecionar dados a partir de critérios
    # | - or
    # & - and
    water = pokemons[(pokemons['Type 1'] == "Water") | (pokemons["Type 2"] == "Water")]
    print(water.head())

    # Para buscar dados não vazios
    doisTipos = pokemons[pokemons["Type 2"].notna()]
    print(doisTipos.head())
    print(doisTipos.shape)

    '''
        A geração de gráficos é facilitada via pandas com a biblioteca matplotlib
        Como exemplo, vamos gerar um gráfico de pizza de pokemons por Type 1.

    '''
    por_tipo = pokemons['Type 1'].value_counts()

    # Cria o gráfico de pizza
    plt.figure(figsize=(8, 8))
    plt.pie(por_tipo, labels=por_tipo.index, autopct='%1.1f%%', startangle=140)
    plt.title("Pokemons por tipo (Type 1)")
    plt.axis('equal')  # Mantém o formato circular
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()