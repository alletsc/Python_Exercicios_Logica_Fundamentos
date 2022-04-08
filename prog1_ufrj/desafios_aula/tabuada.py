""" Tabuada"""

def gera_tabuada():
    print('Gerador de Tabuada')
    num = int(input('Digite um número pra ver a sua tabuada do 1 ao 10: '))
    for n in range(11):
        print(f'{num} x {n} = {num * n}')

gera_tabuada()
