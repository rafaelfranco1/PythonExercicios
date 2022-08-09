
n = int(input("Digite um número ,para calcular seu fatorial: "))
k = n
while (k > 1):
    if (n==2):
        print('2')
    if k == n:
        k = n - 1
        n = n * k

    else :
        k = k -1
        n = n * k
        if (k == 1 and k != n):
            print(n)