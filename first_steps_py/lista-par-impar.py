'''Crie um programa onde o usuário possa digitar sete valores
numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final,
mostre os valores pares e ímpares em ordem crescente.'''

num = [[], []]
val = 0
for c in range(1,8):
    val = int(input(f"Digite o {c}º valor: "))
    if val % 2 == 0:
        num[0].append(val)
    else:
        num[1].append(val)
num[0].sort()
num[1].sort()
print(f"\nOs valores pares são: {num[0]}")
print(f"\nOs valores impares são: {num[1]}.")
