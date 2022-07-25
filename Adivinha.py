import random


x = int(input('Vou pensrm em um número entre 0 e 5. Tente adivinhar...'))
print('Em que número eu pensei? ')
print('PROCESSANDO')

n1 = random.randint(0,5)

if x == n1 :
    print('VOCÊ GANHOU! Adivinhei seu pensamento')
else :
    print('Ganhei! Eu pensei no número {} e não no {}'.format(n1,x))
