N = str(input('Digite seu n ome completo: ')).strip()
nome = N.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))