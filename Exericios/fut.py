'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

jogador = {}
partidas = []
jogador['Nome'] = str(input("Digite o nome do jogador: "))
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0,tot):
    partidas.append(int(input(f"Quantos gols o jogador fez na partida {c+1}? ")))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(f"O jogador {jogador['Nome']}, fez {jogador['total']} gols em {tot} partidas")
print()
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
for i, v in enumerate(jogador['gols']):
    print(f' --Na partida {i+1}, {jogador["Nome"]} fez {v} gols.')
print()
print(jogador)

