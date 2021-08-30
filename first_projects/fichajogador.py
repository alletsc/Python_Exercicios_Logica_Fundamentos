''' Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente.'''

def ficha(jog="> xxxx <", goal=0):
    print(f"{jog} fez {goal} gol(s) no campeonato.")


name = str(input("Nome do jogador: "))
goals = str(input(f'Quantos gols {name} fez no campeonato? '))
if goals.isnumeric():
    goals = int(goals)
else:
    goals = 0
if name.strip() == '':
    ficha(goal=goals)
else:
    ficha(name, goals)
