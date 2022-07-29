cont = 1
acumulador = 0
for cont in range (1,7):
    n = int(input('Digite um número para ser acumulado: '))
    if n % 2 == 0 :
        acumulador = acumulador + n;
print('O acumulador é de: ',acumulador)