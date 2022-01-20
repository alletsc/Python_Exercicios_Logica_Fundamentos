'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

listanum = list()
par = list()
impar = list()
while True:
    num = int(input("Digite um número: "))
    if num not in listanum:
        listanum.append(num)
    else:
        print(f"O valor {num} já se encontra na lista. Tente novamente.")
    r = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    if r == 'N':
        break
for i, v in enumerate(listanum):
    if v % 2 == 1:
        impar.append(v)
    elif v % 2 == 0:
        par.append(v)
print(f'Os valores digitados foram: {listanum}')
print(f'Os numeros pares são: {par}')
print(f"Os numeros impares são: {impar}")
