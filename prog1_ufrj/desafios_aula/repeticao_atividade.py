# Capturando e tratando a quantidade de linhas:
while True:
    try:
        n = int(input('Digite um numero: '))
        if n <= 0:
            print('Valor INVÁLIDO! Digite apenas números inteiros maiores que "0"!')
            n = int(input('Digite um numero: '))
        else:
            break
    except:
        print('Digite apenas números inteiros!')


for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end ='')
        print('  ', end='')
    print()


