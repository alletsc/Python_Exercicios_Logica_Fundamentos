'''Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.'''

reta1 = float(input("Digite o valor do primeiro segmento da reta: "))
reta2 = float(input("Digite o valor do segundo segmento da reta: "))
reta3 = float(input("Digite o valor do terceirio segmentos da reta: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
    print("Você pode formar um triangulo")
else:
    print("Não podemos formar um triangulo")
