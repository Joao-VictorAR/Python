S = float(input('Qual é o salário do Funcionário:'))
N = S + (S*15/100)
print('Um funcionário que ganhava R%{}, com 15% de aumento, passa a receber R%{}'.format(S, N))