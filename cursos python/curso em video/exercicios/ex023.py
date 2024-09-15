Num = int(input('Informe um número: '))
u = Num // 1 % 10
d = Num // 10 % 10
c = Num // 100 % 10
m = Num // 1000 % 10
print('analisando o numero {}'.format(Num))
print('Unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))
