from random import randint

numero_informado = -1
num_secreto = randint(0, 9)

while numero_informado != num_secreto:
    numero_informado = int(input('Informe o número: '))
    print(f'Número secreto {num_secreto} foi encontrado!')
