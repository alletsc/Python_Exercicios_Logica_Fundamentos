# Faça um programa que leia as duas listas e gere uma terceira lista, cujos valores deverão ser compostos pelas somas dos dois valores respectivos a mesma posição.

lista1 = [10, 20, 30, 40]
lista2 = [50, 60, 70, 80]

for i in range(len(lista1)):
    lista3 = lista1[i] + lista2[i]
    print(f'Lista3:\nna {i+1}º posição, temos {lista1[i]} + {lista2[i]} = {lista3}')
