#Crie um programa utilizando while que peça um número de 1 a 10. Caso o usuário digite corretamente, encerre-o. Senão, informar que o número não está entre 1 e 10 e permitir que ele tente novamente.

while True:
    num = int(input('Digite um número de 1 a 10: '))
    if num > 0 and num < 11:
        print(f'O número digitado foi: {num}. E está entre 1 e 10.')
        break
    else:
        print(f"Por favor digite um número entre 1 e 10. Você digitou: {num}. Tente novamente.")
