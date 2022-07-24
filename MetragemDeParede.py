#Cada 2 metros quadrados de parede precisa de 1 litro de tinta para ser pintado
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura*altura
litros = 0.5 * area

print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m²'.format(largura,altura,area))
print('Para pintar essa parede , você precisará de {:.2f}l de tinta'.format(litros))