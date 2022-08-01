#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
acumulador = 0
n = int(input("Digite um número "))
for c in range (1,n+1):
    k = n % c
    if (k == 0):
        print('{} é divisivel por {}'.format(n,c))
        acumulador = acumulador + 1

if (acumulador > 2):
    print('O número {} foi divisível {} vezes'.format(n,acumulador))
    print('E por isso o número {} não é PRIMO'.format(n))
else:
    print('O número {} foi divisível {} vezes'.format(n,acumulador))
    print('E por isso o número {} é PRIMO'.format(n))

