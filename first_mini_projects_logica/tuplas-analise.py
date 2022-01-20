'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

num = (int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")),
        int(input("Digite o terceiro número: ")),int(input("Digite o quarto número: ")))
print(f"Você digitou os valores: {num}")
print(f"O valor nove apareceu {num.count(9)} vezes.")
if 3 in num:
    print(f"O valor 3 apareceu na {num.index(3)+1}ª posição pela primeira vez.")
else:
    print("Nenhum valor 3 digitado.")
print("Os valores pares digitados foram: ")
for n in num:
    if n % 2 == 0:
        print(n, end=" ")