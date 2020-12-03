''' Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso'''

num1 = int(input("Digite um valor: "))
num2 = int(input("Digite outro valor: "))
opcao = 0
while opcao != 5:
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    ''')
    opcao = int(input("Qual opção deseja:  "))
    if opcao == 1:
        soma = num1 + num2
        print(soma)
    elif opcao == 2:
        multiplicar = num1 * num2
        print(multiplicar)
    elif opcao == 3:
        if num1 > num2:
            print("Maior = {}".format(num1))
        else:
            print("Maior = {}".format(num2))
    elif opcao == 4:
        print("Informe os numeros novamente:")
        num1 = int(input("Digite um numero: "))
        num2 = int(input("Digite o segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opção inválida")
print("FIM")
