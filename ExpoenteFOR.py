n1 = int(input("Digite a base: "))
n2 = int(input("Digite o expoente: "))
p = 1
for i in range (1,n2+1):
    p *= n1
print(p)