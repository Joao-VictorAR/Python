N = str(input('Qual é seu nome completo: ')).strip()
N2 = N.lower().find('silva') 
N3 = N2 != -1
print('Seu nome tem Silva? {}'.format(N3))
print('Seu nome tem Silva? {}'.format('silva' in N.lower()))