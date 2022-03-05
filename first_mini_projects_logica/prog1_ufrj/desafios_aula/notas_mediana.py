'''
Um primo seu está estudando estatística e pediu sua ajuda.

Faça um programa que leia 5 notas digitadas pelo usuário e guarde-as em uma lista.

Depois imprima cada nota e imprima também a média e mediana.
'''
import statistics

for i in range(0,5):
    nota = float(input(f'Digite a {i+1}ª nota: '))
    lista = [nota]

print(f"A média das notas digtadas são: {statistics.mean(lista)}")
print(f"A mediana das notas digtadas são: {statistics.median(lista)}")

