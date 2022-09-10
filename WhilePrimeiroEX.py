s = input('Digite seu sexo:')
s1 = s.upper()
cont = 0
while s1 != 'M' or s1 != 'F':
    if cont == 0:
        print('Opção inválida');
        cont = cont + 1

print('Sexo',s,'registrado com sucesso!')