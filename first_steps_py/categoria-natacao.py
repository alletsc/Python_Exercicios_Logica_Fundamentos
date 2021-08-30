''' A Confederação Nacional de Natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

import datetime
atual = datetime.date.today().year

nasc = int(input("Digite seu ano de nascimento: "))
categoria = atual - nasc
print("Voce tem {} anos \nSua categoria é: ".format(categoria))

if categoria <= 9 and categoria < 14:
    print("MIRIM")
elif categoria >= 14 and categoria < 19:
    print("JUNIOR")
elif categoria >=20 and categoria < 25:
    print("SENIOR")
elif categoria >= 25:
    print("MASTER")

