''' Exercício Python 34: Escreva um programa que pergunte o salário de um
funcionário e calcule o valor do seu aumento.
 Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os
 inferiores ou iguais, o aumento é de 15%. '''

salario = float(input("Digite seu salário:  \nUse o . como separador de reais."))

if salario <= 1250:
     novoSalario = salario + (salario*15 /100)
else:
    novoSalario = salario + (salario*10 /100)

print("Seu antigo salário de {:.2f} agora é de {:.2f}".format(salario,novoSalario))