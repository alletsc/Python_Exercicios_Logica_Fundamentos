''' Crie um programa que leia vários números inteiros pelo teclado.
 O programa só vai parar quando o usuário digitar o valor 999, 
 que é a condição de parada. No final, mostre quantos números foram digitados 
 e qual foi a soma entre eles (desconsiderando o flag).'''

n = c = soma = 0
n = int(input(" Para sair digite [999]. \nDigite um numero: "))
while n != 999:
    soma += n
    c += 1
    n = int(input(" Para sair digite [999]. \nDigite um numero: "))
print("Você digitou {} números. \nE a soma entre eles foi: {}".format(c,soma))

