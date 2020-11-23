''' Mostre a tabuada de um número que o usuário escolher, utilizando um laço for'''

num = int(input("Digite um número para ver sua tabuada: "))
print("-*-*-" * 4)
for c in range (1,11):
    print('{} x {} = {} '.format(num, c, num*c))
print("-*-*-" * 4)