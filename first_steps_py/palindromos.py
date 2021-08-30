''' Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.'''

frase = str(input("Digite a frase que quer analisar: ")).strip().upper()

palavrasFrase = frase.split()
palavrasJuntas = "".join(palavrasFrase)
inverso = ""
print("A frase digitada foi {}".format(frase))

for letra in range(len(palavrasJuntas) -1, -1, -1):
    inverso = inverso + palavrasJuntas[letra]
if inverso == palavrasJuntas:
    print("A frase é um PALINDROMO")
else:
    print("A frase não é um palindromo.")
