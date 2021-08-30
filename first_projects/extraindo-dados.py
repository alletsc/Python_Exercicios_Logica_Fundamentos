''' Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitado
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

num = list()
while True:
    n = int(input("DIGITE UM VALOR: "))
    if n not in num:
        num.append(n)
        print(f"Valor {n} adicionado a lista com sucesso.")
    else:
        print( f"Digite outro valor. \n{n} já se encontra na lista.")
    r = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    if r == 'N':
       break
num.sort(reverse=True)
tamanho = len(num)
print("-*-*" * 10)
print(f"Os valores digitados em ordem decrescente foram: {num}")
print(f"A lista contém {tamanho} números.")
if 5 in num:
    print('A lista contém o número 5.')
else:
    print('O número 5 não faz parte da lista.')
print("-*-*" * 10)
