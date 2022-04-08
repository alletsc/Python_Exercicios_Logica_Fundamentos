# Faça um programa que receba 10 medidas e imprima na tela o maior e menor valor recebido.

lista_num = []

for c in range(1, 11):
    lista_num.append(int(input(f'Digite o {c}º número: ')))
    print(lista_num)

print(f'\nO maior número digitado é {max(lista_num)}')
print(f'O menor número digitado é {min(lista_num)}')

