P = float(input('qual é o preço do produto:'))
D = P - (P*5/100)
print('O produto custava{}, na promoção com desconto de 5% vai custar {:.2f}'.format(P, D))