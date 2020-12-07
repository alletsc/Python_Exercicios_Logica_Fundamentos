'''valores = list()
for cont in range (0,5):
    valores.append(int(input("Digite um valor: ")))
print(valores)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Fim da lista')
'''

'''listA = [2,3,4,7]
listB = listA
print(listA)
print(listB)
print(listA[0])'''

'''pessoas = (['Pedro', 25], ['Ana', 36], ['Joao',78])
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])'''

'''teste = list()
teste.append('Stella')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Josi'
teste[1] = 23
galera.append(teste[:])
print(galera)'''

'''galera = [['João', 25],['Ana', 34],['Stella', 23]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''


'''
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen +=1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
'''


