'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

dados = {}
org = []
soma = media = 0
while True:
    dados.clear()
    dados['nome']=str(input("Nome: "))
    while True:
        dados['sexo']=str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dados['sexo'] in 'FM':
            break
        print('Por favor, responda com apenas F ou M.')
    dados['idade']=int(input("Idade: "))
    soma += dados['idade']
    org.append(dados.copy())
    while True:
        r = str(input("Deseja continuar? [S/N] ")).upper()[0]
        if r in 'SN':
            break
        print('ERRO! Responda apenas com S ou N.')
    if r == 'N':
        break
print("---"*20)
print(f"Ao todo temos {len(org)} pessoas cadastradas.\n")
media = soma / len(org)
print(f'A média de idades é de {media:5.2f} anos')
print("---"*20)
print(f'As mulheres cadastradas foram: ', end=' ')
for p in org:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end=' ')
print('Pessoas acima da média: ', end=' ')
for p in org:
    if p['idade'] >= media:
        print(" ")
        for k, v in p.items():
            print(f'{k} = {v}; ', end=' ' )
            