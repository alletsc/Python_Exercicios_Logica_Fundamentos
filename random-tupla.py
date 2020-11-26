'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint
num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f"Os numero sorteados foram: {num}")
for c in num:
    print(f'{c}', end= " ")
print(f"\nO maior valor é {max(num)}")
print(f"O menor valor é: {min(num)}")

