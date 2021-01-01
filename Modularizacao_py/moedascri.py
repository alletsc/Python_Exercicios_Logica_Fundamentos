import moeda

preco = float(input("Digite o preço: R$"))
print(f'A metade do preço é {moeda.metade(preco)}.')
print(f'O dobro do preço é {moeda.dobro(preco)}.')
print(f"{preco} menos  em  10% = {moeda.diminuir(preco,10)}")
print(f"{preco} mais 10%  = {moeda.aumentar(preco,10)}")
