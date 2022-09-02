n = int(input("Digite o número de vezes : "))

i = 1;
soma = 0
for i in range (n):
    if (i % 5 == 0):

        i = i + 5
        soma = soma + i

print(soma)