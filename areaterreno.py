'''Faça um programa que tenha uma função chamada área(), que receba as
dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def area(lar, comp):
    a = lar * comp
    print(f"A area de um terreno: {comp} x {lar} = {a}m².")


print('Controle de area')
print("-" * 20)
l = float(input("Largura em (metros): "))
c = float(input("Comprimento (em metros): "))
area(l, c)
