'''  Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep

def mai(*num):
    cont = mai = 0
    print(f'-=-' * 10)
    print("Análise concluída:")
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            mai = valor
        else:
            if valor > mai:
                mai = valor
        cont += 1
    print(f'\nForam informados {cont} valores')
    print(f'O maior valor é: {mai}')
    print(f'-=-' * 10)
    print()


mai(2, 9, 4, 5, 7, 1)
mai(7,9,23,56,1,0)
mai(1,2)
mai(9)
mai()