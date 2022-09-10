soma = 0;
n1 = int(input("Digite o inicio do intervalo : "))
n2 = int(input("Digite o fim do intervalo : "))
while (n1 <= n2):
    if n1 % 2 == 0 and n1 % 7 == 0:
        print(n1)
    n1 = n1 + 1
