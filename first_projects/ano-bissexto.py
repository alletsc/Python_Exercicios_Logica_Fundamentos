''' Faça um programa que leia um ano qualquer e mostre se ele é bissexto'''

from datetime import date
ano = int(input("Que ano você quer analisar? Digite 0 para analisar o ano atual. "))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano != 0 or ano % 400 ==0:
    print("Ano bissexto")
else:
    print("Não é bissexto")
