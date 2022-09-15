i = 1
negativo = 0
while i <= 2:
    n = int(input('Digite um valor,para ser computado se vai ser negativo ou não: '))
    if (n < 0):
        negativo = negativo + 1
    i=i+1
print('Possui',negativo,'numeros negativos')