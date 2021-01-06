''' Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

listanum = list()
for c in range (0,5):
    n = int(input("Digite um valor: "))
    if c == 0 or n > listanum[-1]:
        listanum.append(n)
    else:
        pos = 0
        while pos < len(listanum):
            if n <= listanum[pos]:
                listanum.insert(pos, n)
                break
            pos =+1
print(f"Os valores digitados foramm: {listanum}")
