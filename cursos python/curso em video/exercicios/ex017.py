import math
CO = float(input('Comprimento do cateto oposto: '))
CA = float(input('Comprimento do cateto adjacente: '))
H = math.hypot(CO, CA)
print('A hipotenusa vai medir {:.2f}'.format(H))