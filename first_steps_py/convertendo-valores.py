'''Escreva um programa em Python que leia um número inteiro qualquer e peça
para o usuário escolher qual será a base de conversão:
 1 para binário, 2 para octal e 3 para hexadecimal.'''

numero = int(input("Digite um valor: "))
print("Escolha uma base para converão: \n[1] binário \n[2] octal \n[3] hexadecimal \n")
conversao = int(input('Digite sua opção: '))

if conversao == 1:
    print("O número {} em binário equivale a {}".format(numero, bin(numero)[2:]))
if conversao == 2:
    print("O número {} em octal equivale a {}".format(numero, oct(numero)[2:]))
if conversao == 3:
    print("O número {} em hexadecimal equivale a {}".format(numero, hex(numero)[2:]))

else:
    print("Opção inválida.") 
