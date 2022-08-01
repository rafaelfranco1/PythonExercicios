n1=int(input("Primeiro elemento: ") )
r = int(input("Razao: ") )

for c in range (0,11):
    if n1 >= 0 and c < 10:
        print(n1,' -> ',end='')
        n1 = n1 + r
    if c == 10:

        print(n1)






