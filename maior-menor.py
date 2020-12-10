'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''


valor = list()
mai = 0
men = 0
for c in range(0,5):
    valor.append(int(input(f"DIGITE UM VALOR PARA POSIÇÃO {c}: ")))
    if c ==0:
        mai = men = valor[c]
    else:
        if valor[c] > mai:
            mai = valor[c]
        if valor[c] < men:
            men = valor[c]
print(f"Maior valor: {mai} \nE menor valor: {men}")
for i, v in enumerate(valor):
    if v == mai:
        print(f"Maior valor na {i+1}ª posição.")
for i, v in enumerate(valor):
    if v == men:
        print(f'Menor valor na {i+1}ª posição.')
print()