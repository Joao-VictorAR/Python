d = int(input('quantos dias o carro foi alugado:'))
km = float(input('quantos km o carro andou:'))
p = (d * 60) + (km * 0.15)
print('o total a pagar é de R${:.2f}'.format(p))