# Faca um programa que calcule o imc de uma pessoa.

# O programa deve solicitar o peso e a altura e aplicar a tabela de imc abaixo.

# É obrigatório o uso de if com else ou elif

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)
print(f"Seu IMC é de {imc:.2f}")
if imc < 18.5:
    print('Você está abaixo do peso normal.')
elif imc >= 18.5 and imc < 24.9:
    print('Você está no peso normal.')
elif imc >= 25 and imc < 29.9:
    print('Você está com sobrepeso.')
elif imc >= 30 and imc < 34.9:
    print('Você está com obesidade grau I.')
elif imc >= 35 and imc < 39.9:
    print('Você está com obesidade grau II.')
else:
    print('Você está com obesidade grau III.')
