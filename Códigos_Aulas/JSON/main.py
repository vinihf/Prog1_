import json

def main():
    timesFutebol = [{'nome':"Grêmio", "Libertadores":3},
                    {'nome':"Internacional","Libertadores": 2}]

    # Converter para JSON
    emJSON = json.dumps(timesFutebol,ensure_ascii=False, indent=4)
    print(emJSON)

    # Salvar JSON em um arquivo .json
    with open("times.json","w",encoding="utf-8") as arquivo:
        json.dump(timesFutebol,arquivo, ensure_ascii=False,indent=4)

    # Recuperar o conteudo
    with open("times.json","r",encoding="utf-8") as file:
        times_do_arquivo_JSON = json.load(file)

    for time in times_do_arquivo_JSON:
        print(f'{time['nome']} - {time['Libertadores']}')

if __name__ == "__main__":
    main()


