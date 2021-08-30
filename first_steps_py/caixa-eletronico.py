'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e
o programa vai informar quantas cédulas de cada valor serão entregues.
OBS:considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print("====" * 10)
print("{:^40}".format("Simulador de caixa eletrônico V1.0"))
print("====" * 10)
saque = int(input("Quanto deseja sacar? R$"))
vf = saque
nota = 50
totnota = 0
while True:
    if vf >= nota:
        vf -= nota
        totnota += 1
    else:
        if totnota > 0:
            print(f"Total de {totnota} notas de R${nota}")
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totnota = 0
        if vf == 0:
            break
print("Fim")
