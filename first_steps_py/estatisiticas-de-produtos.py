'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

tot = totp1000 = menorp = cont = 0
pbarato = " "
while True:
    produto = str(input("Produto: "))
    preco = float(input("Preço: R$"))
    cont += 1
    tot += preco
    if preco  > 1000:
        totp1000 +=1
    if cont == 1 or preco < menor:
        menor = preco
        pbarato = produto
    resp = ' '
    while resp not in "SN":
        resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if resp == "N":
        break
print("{:-^40}".format("Fim do programa"))
print(f'Total de compras = R$ {tot:.2f}')
print(f"{totp1000} produtos acima de R$1000,00")
print(f"O produto mais barato foi {pbarato} e custa R${menor:.2f}")
