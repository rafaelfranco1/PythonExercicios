tabuada = int(input('Digite um número para ver sua tabuada: '))
cont = 0

for cont in range (0,11):
    multiplicador = cont * tabuada
    print('{} x {} = {}'.format(tabuada,cont,multiplicador))