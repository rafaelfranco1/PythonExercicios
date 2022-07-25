#fatiando com dois pontos , para pegar um determinado tamanho
lista = ['R','a','f','a','e','l','F','r','a','n','c','o']
print(lista[:5]) #o inverso é válido [5:]
#Retorno - ['R', 'a', 'f', 'a', 'e']


lista2 = ['c','u','r','s','o',' ','e','m',' ','v','i','d','e','o',' ','p','y',
          't','h','o','n']
print(lista2[9])
#retorno - v

#Pulando
'''Começa do 9 até o fim . Pula de 3 em 3 cortando as letras antes
A primeira letra conta como 1 , ou seja corta as duas próximas letras '''
print(lista2[9::3])
#frase[9:21:2]
Começa no 9 , vai até o 21 pulando de 2 em 2

#len(x)-> mostra o comprimento da String

#frase.count('o') -> quantas vezes aparece o 'o' minusculo somente .
#frase.count('o',0,13)-> quantas vezes o caracter 'o' aparece do zero ao 13
#frase.find('deo') -> em que momento começou a aparecer o deo
#quando o valor é -1 , não foi encontrado o que busca na string
#Curso in frase -> TRUE escreve true

lista3 = ['c','u','r','s','o',' ','e','m',' ','v','i','d','e','o',' ','p','y','t','h','o','n']
print(lista3[9::4])

#omitindo :5 significa começar em zero
#frase.replace('Python','Android')
#capitalize só o primeiro caracter em maíusculo
#title após o espaço letra maíuscula
#strip() removo espaços do começo e do final , rstrip , lstrip lógicamente
#spilt gera uma nova lista , para cada palavra em espaços de uma string
#::2 SOMENTO O NÚMERO INDICIA O PULO