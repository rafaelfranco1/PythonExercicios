import random
n1 = input("Primeiro ALuno: ")
n2 = input("Segundo Aluno: ")
n3 = input("Terceiro Aluno: ")
n4 = input("Quarto Aluno: ")

lista = [n1,n2,n3,n4]
w = random.sample(lista,k = 4)
print('O aluno sorteado foi {}'.format(w))
print(random.shuffle(lista))

'''
Syntax : random.sample(sequence, k)

Parameters:
sequence: Can be a list, tuple, string, or set.
k: An Integer value, it specify the length of a sample.

Returns: k length new list of elements chosen from the sequence.'''
