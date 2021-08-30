''' Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas.
    B) Uma listagem com as pessoas mais pesadas.
    C) Uma listagem com as pessoas mais leves.'''

temp = list()
prin= list()
mai = men = 0
while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input('Peso: ')))
    if len(prin) == 0:
        mai == men == temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    prin.append(temp[:])
    temp.clear()
    resp = str(input("Deseja continuar [S/N] ? ")).strip().upper()[0]
    if resp == 'N':
        break
print(f'\nOs valores digitados foram: {prin}')
print(f"\nVocê cadastrou {len(prin)} pessoas ")
print(f"\nMAIOR PESO: {mai} KG")
print(f"MENOR PESO: {men} KG\n")
#continuar