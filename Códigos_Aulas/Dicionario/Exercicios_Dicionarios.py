'''def exercicio1():
    semana = {
        "Segunda-feira":{"Disciplina":"Lógica","Créditos":4},
        "Terça-feira":["Matemática 1"],
        "Quarta-feira":["Programação 1"],
        "Quinta-feira":["Português", "Inglês"],
        "Sexta-feira":["Fundamentos da Computação"]
    }
    semana["Quinta-feira"][1]
'''
def exercicio2():
    regioes = {"sul":[],"sudeste":[]}
    while True:
        sigla = input("Informe a sigla")
        if sigla in ["RS","SC","PR"]:
            if sigla not in regioes['sul']:
                regioes["sul"].append(sigla)
        elif sigla in ["SP","MG","ES","RJ"]:
            if sigla not in regioes['sudeste']:
                regioes["sudeste"].append(sigla)
        else:
            print("Sigla não corresponde a região sul ou sudeste")
        continua = input("Mais? (S)im ou (N)ão")
        if continua == "N":
            break
    print(regioes)

def exercicio3():
    agenda = {}
    while True:
        cpf = input("CPF:")
        nome = input("Nome:")
        idade = int(input("Idade:"))
        telefone = input("Telefone:")
        agenda[cpf] = {"nome":nome,"idade":idade,"telefone":telefone}
        continuar = input("Continuar? (S)im ou (N)ão")
        if continuar == "N":
            break
    for chave in agenda:
        print(f'{agenda[chave]['nome']} - {agenda[chave]['idade']} ({agenda[chave]['telefone']})')


if __name__ == "__main__":
    exercicio3()