produto = {'nome': 'Caneta Chic', 'preco': 14.99,
           'importada': True, 'estoque': 793}

for c in produto:
    print(c)
print('=-='*10)

for v in produto.values():
    print(v)
print('=-='*10)

for c, v in produto.items():
    print(c, '=', v)
print(c, v)
