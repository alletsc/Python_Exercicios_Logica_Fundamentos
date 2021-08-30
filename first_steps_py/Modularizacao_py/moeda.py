def aumentar(preco = 0, taxa = 0, formatado=False):
    res = preco + (preco * taxa /100)
    return res if formatado is False else moeda(res)


def diminuir(preco = 0, taxa = 0, formatado=False):
    res = preco - (preco * taxa /100)
    return res if formatado is False else moeda(res)


def dobro(preco=0, formatado=False):
    res = preco * 2
    return res if not formatado else moeda(res)


def metade(preco=0, formatado=False):
    res = preco / 2
    return res if not formatado else moeda(res)

def moeda(preco = 0, moeda = "R$"):
    return (f'{moeda}{preco:>.2f}'.replace(".", ","))

def resumo(preco=0, taxaa=10, taxar=5 ):
    print("=-=" * 10)
    print('Resumo do Valor:'.center(30))
    print("=-=" * 10)
    print(f"Preço analisado: {moeda(preco)}")
    print(f'\nDobro: \t\t\t{dobro(preco, True)}')
    print(f"Metade: \t\t{metade(preco, True)}")
    print(f"Com desconto de {taxar}%: \t{diminuir(preco, taxar, True)}")
    print(f"Com Aumento de {taxaa}%: \t{aumentar(preco, taxaa, True)}\n")
    print("=-=" * 10)