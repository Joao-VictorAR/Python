L = float(input('qual a largura da parade:'))
A = float(input('qual a altura da parade:'))
area = A*L
T = area/2
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m²'.format(L, A, area))
print(' Para pintar essa parede, você precisará de {} de tinta'.format(T))