from random import randint
from time import sleep

def sorteia(lista):
    for cont in range(0, 5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ', end=' - ')
        sleep(0.3)
    print('\n\nSORTEIO CONCLUÍDO!!!')


def somapar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'\nSoma dos valores pares igual á: {soma}.')
    print()

num = list()
sorteia(num)
print(num)
somapar(num)