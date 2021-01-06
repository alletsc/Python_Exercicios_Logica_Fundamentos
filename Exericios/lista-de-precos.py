''' Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
print('====' * 10)
print(f'{"LISTA DE PREÇOS":^40}')
print('====' * 10)
prod = ("Lápis", 0.75, "Livro", 11.85, "Borracha", 15.90,
        "Caderno", 9.99, "Caneta", 1.25)
print
for item in range(0, len(prod)):
    if item % 2 == 0:
        print(f"{prod[item]:.<30}", end="")
    else:
        print(f"R${prod[item]:>7.2f}")
print('====' * 10)
print('====' * 10)