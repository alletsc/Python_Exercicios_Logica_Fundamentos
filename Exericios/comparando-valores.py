'''Escreva um programa que leia dois números inteiros e compare-os. mostrando
 na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais '''

num = float(input("Digite um valor: "))
num1 = float(input("Digite outro valor: "))
if num > num1:
    print("O primeiro valor é maior.")
if num == num1:
    print("Não existe valor maior, os dois são iguais")
else:
    print("O segundo valor é maior.")