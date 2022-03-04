"""
Um cinema tem preços diferenciados dependendo da idade da pessoa.

Se a pessoa tem menos de três de anos, o ingresso é de graça;
Se a pessoa tem entre 3 e 12 anos, o ingresso é 10,00;
E se a pessoa tem mais de 12 anos, o ingresso é 15,00.
Escreva um programa utilizando while condicional no qual tenha um menu:
- sair
- você pergunta ao usuário a idade e depois retorna o preço do ingresso.
"""
import os


def compra_ingresso():
    try:
        total = 0
        ingresso = 0
        while True:
            print(f'Bem vindo ao nosso cinema!')
            print('Para sair digite "sair"')
            print('Para cancelar o seu pedido digite "000"')
            quant = int(input('Quantos ingressos deseja comprar: '))
            if quant == 000:
                print('Pedido cancelado.')
                continue
            for i in range(quant):
                idade = int(input('Qual a idade da pessoa: '))
                if idade < 3:
                    ingresso = 0
                elif idade >= 3 and idade <= 12:
                    ingresso = 10
                else:
                    ingresso = 15
                total += ingresso
                print(f'O total a pagar é de R${total}')
            os.system('clear')
    except ValueError:
        print('Obrigado por utilizar nosso sistema!')
        print("Saindo...")


compra_ingresso()
