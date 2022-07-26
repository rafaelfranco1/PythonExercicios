ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0 :
    print("O ano de 2022 , não é bissexto")
elif ano % 100 == 0 and ano % 400 != 0 :
    print('O ano não é bissexto')
elif ano % 4 == 0:
    print("O ano é bissexto")
else :
    print("O ano não é bissexto")