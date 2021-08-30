'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import datetime

dados = {}
dados['Nome'] = str(input('Nome: '))
nasc = int(input("Ano de nascimento: "))
dados['idade']= datetime.now().year - nasc
dados['ctps']=int(input("Carteira de trabalho (0000: não tem): "))
if dados['ctps'] != 0:
    dados['contratacao']= int(input("Ano de contratação: "))
    dados['salario'] = float(input("Salário: R$"))
    dados['aposentadoria'] = (dados['contratacao'] + 35 + dados['idade']) - datetime.now().year
    print('=-=' * 30)
for k, v in dados.items():
    print(f"-- {k} tem valor: {v}")
print('=-=' * 30)
