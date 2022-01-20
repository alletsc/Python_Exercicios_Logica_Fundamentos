''' Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
 se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''


import datetime

nascimento = int(input("Digite seu ano de nascimento: "))

hoje = datetime.date.today().year
idade = hoje - nascimento

print("Você tem {} anos.".format(idade))
if idade > 18:
    passou = idade - 18
    alistamento = hoje - passou
    print("Você deveria ter se alistado há {} anos! \nAliste-se imediatamente"
          .format(passou))
    print("Seu alistamento foi em {}.".format(alistamento))
elif idade == 18:
    print("Você deve se alistar imediatamente.")

elif idade < 18:
    falta = 18 - idade
    alistamentoFalta = hoje + falta
    print("Voce deverá se alistar em {} anos.\nSeu alistamento será no ano de {}"
          .format(falta, alistamentoFalta))
          