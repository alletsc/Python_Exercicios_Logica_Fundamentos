time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['Nome'] = str(input("Digite o nome do jogador: "))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f"Quantos gols o jogador fez na partida {c+1}? ")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            break
        print("Responda apenas S ou N.")
    if r == 'N':
        break
print('-=' * 30)
print('COD ', end='')
for i in jogador.keys():
    print(f"{i:<15}", end='')
print()
print('-=' * 30)
for k, v in enumerate(time):
    print(f" {k:>3} ", end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Mostrar dados de qual jogador? '))
    if busca == 9999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe o jogador de código {busca}')
    else:
        print(f'Levantamento do jogador: {time[busca]["Nome"]} ')
        for i, g in enumerate(time[busca]['gols']):
            print(f' No jogoj {i} fez {g} gols.')
    print("---" * 10)
print("Fim")