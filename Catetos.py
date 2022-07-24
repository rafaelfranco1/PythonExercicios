import math
oposto = float(input('Comprimento do cateto oposto: '))
adj = float(input('Comprimento do cateto adjacente: '))
soma = pow(oposto,2) + pow(adj,2)
hip = math.sqrt(soma)
print('A hipotenusa vai medir {}'.format(hip))