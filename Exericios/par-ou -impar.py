''' Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo'''

from random import randint

print("--*--" * 10)
print("PAR OU IMPAR?")
print("--*--" * 10)

v = 0
while True:
    jog = int(input('Digite um valor: '))
    comp = randint(0, 10)
    tot = jog + comp
    p_or_i = ' '
    while p_or_i not in "PI":
        p_or_i = str(input('Par ou ímpar? [P/I]:  ')).strip().upper()[0]
    print(f"Voce jogou {jog} e o computador {comp}. Total = {tot}.")
    print("DEU PAR!!!" if tot % 2 == 0 else "DEU IMPAR!")
    if p_or_i == "P":
        if tot % 2 == 0:
            print('Voce venceu!!!')
            v += 1
        else:
            print("Voce perdeu.")
            break
    elif p_or_i == 'I':
        if tot % 2 == 1:
            print('Voce venceu!!!')
            v += 1
        else:
            print("Voce perdeu.")
            break
    print("Vamos mais uma vez!!!")
print(f"Voce venceu {v} vezes. \nGAME OVER")
