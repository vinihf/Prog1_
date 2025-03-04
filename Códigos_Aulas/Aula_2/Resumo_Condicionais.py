'''
Um programa, até aqui, nos permite construir instruções que são seguidas em sua totalidade.
Porém, para que possamos construir programas mais complexos, precisamos poder adicionar
desvios que somente serão executados se atenderem a uma determinada condição

As estruturas que nos permitem trabalhar condições nos códigos são as estruturas condicionais.
Estas estruturas são representadas pelas palavras reservadas if, else e elif.
Mais recentemente  foi adicionada a instrução match.

Para construir estruturas condicionais, precisamos utilizar operadores relacionais:
> - maior que
< - menor que
>= - maior ou igual
<= - menor ou igual
== - igual
'''

nome = input("Informe seu nome:")
idade = int(input("Informe sua idade:"))
if idade >= 18:
    print(f'{nome} é maior de idade.')
else:
    print(f'{nome} é menor de idade.')

''' Vamos pegar o caso dos beneficiários do Bolsa Família.

https://www.gov.br/mds/pt-br/acoes-e-programas/bolsa-familia

'''

renda_total = float(input("Informe a renda da família:"))
pessoas_familia = int(input("Informe quantas pessoas constituem a família:"))
if (renda_total/pessoas_familia) < 218:
    print("Aprovado")
else:
    print("Reprovado")

'''
Mas, observe, é preciso primeiro estar cadastrado no Cadastro Único

Aqui vamos utilizar operadores lógicos. São eles:
and = E
or = OU
not = NÃO
'''

renda_total = float(input("Informe a renda da família:"))
pessoas_familia = int(input("Informe quantas pessoas constituem a família:"))
cadastro_unico = input("Família no Cadastro Único? (S)im ou (N)ão")
if ((renda_total/pessoas_familia) < 218) and cadastro_unico == "S":
    print("Aprovado")
else:
    print("Reprovado")