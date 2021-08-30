''' Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
num = int(input("Digite um número: "))
total = 0
for c in range(1, num +1):
    if num % c == 0:
        print("\033[32m", end=" ")
        total = total + 1
    else:
        print("\033[31m", end=" ")
    print("{}".format(c), end=" ")
print("\n\033[0;0mO número {} foi divisivel {} vezes.".format(num,total ))
if total ==2:
    print("Número primo.")
else:
    print("Não é primo.")
