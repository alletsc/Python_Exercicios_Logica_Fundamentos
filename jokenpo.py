'''Crie um programa que faça o computador jogar Jokenpô'''
# CORRIGIR ERRO


from random import randint
from time import sleep

opcoes = ('Pedra', 'Papel', 'Tesoura')
print('''Escolha uma opção:\n
[0] Pedra
[1] Papel 
[2] Tesoura \n''')

computador == randint(0,2)

jogador = int(input('Qual a sua jogada? \n'))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")

print("--*--*--*--*" * 9)
print("Você escolheu a opção {}.".format(opcoes[jogador]))
print("O computador escolheu: {}.".format(opcoes[computador]))
print("--*--*--*--*" * 9)

if computador == 0:  # Pedra
    if jogador == 0:
        print("Empate")
    elif jogador == 1:
        print("Você venceu!")
    elif jogador == 2:
        print("Você perdeu!")

elif computador == 1:  # Papel
    if jogador == 1:
        print("Empate")
    elif jogador == 0:
        print("Você perdeu!")
    elif jogador == 2:
        print("Você venceu!")
    else:
        print("Jogada inválida. \nTENTE NOVAMENTE!")

elif computador == 2:  # Tesoura
    if jogador == 2:
        print("Empate")
    elif jogador == 0:
        print("Você venceu!")
    elif jogador == 1:
        print("Você perdeu!")
    else:
        print("Jogada inválida. \nTENTE NOVAMENTE!")

else:
    print("Jogada inválida. \nTENTE NOVAMENTE!")