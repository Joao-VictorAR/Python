import math
Angulo = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(Angulo))
print('O ângulo de {} tem o seno de {:.2f}'.format(Angulo, seno))
cosseno = math.cos(math.radians(Angulo))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(Angulo, cosseno))
tangente = math.tan(math.radians(Angulo))
print('O ângulo de {} tem a tangente de {:.2f}'.format(Angulo, tangente))

