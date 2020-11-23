#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

valor1=input("Digite o primeiro valor:")
valor2=input("Digite o segundo valor:")
valor3=input("Digite o terceiro valor:")

menor = valor1
if valor2 < valor1 and valor2 < valor3:
    menor = valor2
if valor3 < valor1 and valor3 < valor2:
    menor = valor3
print("O menor valor digitado foi {}".format(menor))


maior = valor1
if valor2 > valor1 and valor2 > valor3:
    maior = valor2
if valor3 > valor1 and valor3 > valor2:
    maior = valor3
print("O maior valor digitado foi {}".format(maior))