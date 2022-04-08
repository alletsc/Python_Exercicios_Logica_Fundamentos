def calcula_fatorial():
    n = int(input('Digite um número: '))
    fat = 1
    for i in range(1, n+1):
        fat *= i
    print(f'O fatorial de {n} é {fat}')

calcula_fatorial()
