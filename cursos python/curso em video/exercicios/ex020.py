import random
A1 = str(input('Primeiro aluno: '))
A2 = str(input('Segundo aluno: '))
A3 = str(input('Terceiro aluno: '))
A4 = str(input('Quarto aluno: '))
Lista = [A1, A2, A3, A4]
random.shuffle(Lista)
print('A ordem de apresentação será')
print(Lista)