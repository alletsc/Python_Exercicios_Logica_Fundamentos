def jogar_forca():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    secret_word = 'banana'.upper()
    acertou = False
    enforcou = False

    while True:
        chute = input('Digite uma letra: ').upper()

        index = 0
        for letra in secret_word:
            if chute == letra:
                print(f'encontrei a letra {letra} na posição {index}.')

            index += 1

        print('Jogando...')

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar_forca()
