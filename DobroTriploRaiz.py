import math
#Dobro, Tripo, Raiz Quadrada
n1 = float(input('Digite um número :'))
dobro = 2 * n1
triplo = 3 * n1
raiz = math.sqrt(n1)
print('O dobro de {} vale {}'.format(n1,dobro))
print('O tripo de {} vale {}'.format(n1,triplo))
print('A raiz quadrada de {} é igual a {:.3f}'.format(n1,raiz))
