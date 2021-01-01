import moeda

preco = float(input("Digite o preço: R$"))
print(f'A metade do preço é {moeda.metade(preco, True)}.')
print(f'O dobro do preço é {moeda.dobro(preco, True)}.')
print(f"{moeda.moeda(preco)} menos 10% = {moeda.diminuir(preco, 13, True)}")
print(f"{moeda.moeda(preco)} mais 10%  = {moeda.aumentar(preco, 10, True)}")
