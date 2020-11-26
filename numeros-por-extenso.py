''' Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 15) e mostrá-lo por extenso.'''

#num = int(input("Digite um número: "))
#print(f"Você digitou {}")
cont =("zero", "um", "dois", "tres", 'quatro', 'cinco',
'seis','sete', 'oito', 'nove,','dez',
'onze','doze', 'treze','quatorze','quinze')
while True:
    num = int(input('Digite um numero entre 0 e 15: '))
    if 0 <= num <= 15:
        break
    print("Tente novamente.")
print(f"Você digitou: {cont[num]}.")