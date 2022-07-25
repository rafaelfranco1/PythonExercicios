import string
lista3 = ['c','u','r','s','o',' ','e','m',' ','v','i','d','e','o',' ','p','y','t','h','o','n']

#Printa a Lista De 9 até 21 ou seja Vídeo Python com um Pulo de Dois em Dois
print(lista3[9:21:2])

#Troca todas as letras 'o' por Couglas . O método replace retorna uma string não uma lista , por isso há necessidade de usar for
replaced = [i.replace('o','Couglas') for i in lista3]
print(replaced)

replaced2 = [i.replace('python','Android') for i in lista3]

print(replaced2)

lista4 = 'Curso em video Python'
k = lista4.replace('Python','Android')
print(k)

J = lista4.replace('o','Couglas')
print(J)

w = lista4.split()

final = lista4.replace('w[o]','Couglas')

print(final)