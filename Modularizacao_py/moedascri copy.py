import moeda

preco = float(input("Digite o preço: R$"))
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}.')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}.')
print(f"{preco} menos 10% = {moeda.moeda(moeda.diminuir(preco,10))}")
print(f"{preco} mais 10%  = {moeda.moeda(moeda.aumentar(preco,10))}")

