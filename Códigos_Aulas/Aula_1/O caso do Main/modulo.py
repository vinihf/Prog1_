modulo.py

'''

Um arquivo .py pode ser tratado como um script ou como um módulo.

Um script é um arquivo que pretende-se executar no terminal ou via entrada de usuário.
Um módulo é um arquivo que pretende-se importar em um script.

A variável que registra essa informação é nomeada __name__.

Seu valor varia de acordo com a forma da execução de um arquivo.

'''

print(f'Vamos observar a diferença entre execução: {__name__}')