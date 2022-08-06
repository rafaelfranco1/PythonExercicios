m = 0
x = int(input('Digite n1:'))
y = int(input('Digite n2:'))
while m != 5:
    print('Qual sua opção:')
    print('1 - Somar')
    print('2 - Multiplicar')
    print('3 - Maior')
    print('4 - Novos números')
    print('5 - Sair do programa')
    m = int(input("Qual a sua opção?"))
    if (m == 1):
        w = x + y
        print(w)
    elif (m ==2):
        w = x * y
        print(w)
    elif(m==3):
        if x > y :
            print(x)
        elif (y > x):
            print(y)
        else:
            print('iguais')
    elif (m==4):
        x = int(input("Digite x"))
        y = int(input("Digite y"))

    elif (m==5):
        print('Voce saiu')
    else:
        print('Opcao invalida tente novamente:')
        m = int(input("Qual a sua opção?"))