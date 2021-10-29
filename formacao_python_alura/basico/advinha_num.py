import random


def jogar_advinhacao():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    secret_num = round(random.randrange(1, 100))
    rodada = 1

    print('''Dificuldades:
    >>> [1] facil [2] medio [3] dificil\n''')
    dif = int(input("Digite o num correspondente a dificulade do seu jogo: "))

    if dif == 1:
        tentativas = 5
    elif dif == 2:
        tentativas = 3
    elif dif == 3:
        tentativas = 1
    else:
        print('Escolha a dificuldade.')

    while tentativas > 0:
        print(f'Tentativa {rodada} de {tentativas}')
        chute = int(input('Digite um número inteiro entre 0 e 100: '))
        print(f'Voce digitou o numero inteiro {chute}.\n')

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = secret_num == chute
        maior = secret_num < chute
        menor = secret_num > chute

        if acertou:
            print('Voce acertou!\n')
            break
        else:
            if maior:
                print('Vc tentou um chute maior que o numero secreto.\n')
            if menor:
                print('Seu chute é menor que o numero secreto.\n')
        tentativas = tentativas - 1
        rodada = rodada + 1
    print('FIM DE JOGO!!!\n')
    print(f'O numero secreto era {secret_num}')


if (__name__ == "__main__"):
    jogar_advinhacao()
