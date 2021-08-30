from random import randint
computador = randint(0, 10)
print("Sou o seu computador e acabei de pensar em um numero entre 0 e 10. \nTe desafio a advinhar qual foi!")
acertou = False
palpite = 0
while not acertou:
    jogador = int(input("Digite o seu palpite: "))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais...")
        elif jogador > computador:
            print("Menos...")
print("ACERTOU! Com {} palpites.".format(palpite))

