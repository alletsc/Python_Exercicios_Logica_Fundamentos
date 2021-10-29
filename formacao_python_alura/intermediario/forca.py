import random


def bem_vindo():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def palavra_secreta():
    palavras = []
    with open('intermediario/palavras.txt') as arq:
        for linha in arq:
            linha = linha.strip()
            palavras.append(linha)

    num = random.randrange(0, len(palavras))
    palavra_sec = palavras[num].upper()
    return palavra_sec


def pede_chute():
    chute = input('Qual a letra? ').strip().upper()
    return chute


def perdeu():
    print("    Você foi enforcado!      ")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def venceu():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar_forca():
    bem_vindo()

    palavra_sec = palavra_secreta()

    letras_corretas = ["_" for letra in palavra_sec]

    acertou = False
    enforcou = False
    erros = 0

    while (not enforcou and not acertou):
        chute = pede_chute()
        if chute in palavra_sec:
            index = 0
            for letra in palavra_sec:
                if chute == letra:
                    letras_corretas[index] = letra
                index += 1
            print(letras_corretas)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 6
        acertou = '_' not in letras_corretas
        print(letras_corretas)

    if acertou:
        venceu()
    else:
        perdeu()
        print(f'A palava secreta era {palavra_sec}')


if (__name__ == "__main__"):
    jogar_forca()
