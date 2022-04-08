# Faça um programa que leia duas strings e informe o conteúdo delas seguido do seu comprimento

frase1 = input('Digite uma Frase: ')
frase2 = input('Digite outra Frase: ')

print(f'String 1: {frase1}')
print(f'String 2: {frase2}')
# Print formatado, contando caracteres e excluindo espaços em branco.
print(f'Comprimento da String 1: {len(frase1.replace(" ", ""))} caracteres')
print(f'Comprimento da String 2: {len(frase2.replace(" ", ""))} caracteres.')
