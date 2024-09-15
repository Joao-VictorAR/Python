F = str(input('Digite uma frase:')).strip()
print('A letra A aparece {} vezes na frase'.format(F.lower().count('a')))
print('A primeira letra A apareceu na posição {}'.format(F.lower().find('a')+1))
print('A ultima letra A apareceu na posição {}'.format(F.lower().rfind('a')))