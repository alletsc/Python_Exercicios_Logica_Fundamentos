'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = float((nota1 + nota2) / 2)
total = media
print("Sua média foi {}.".format(media))
if media <= 5:
    print("Você está reprovado.")
elif media > 5 and media <= 6.9:
    print("Você está em recuperação")

elif media >= 7:
    print("Parabéns, você foi aprovado.")