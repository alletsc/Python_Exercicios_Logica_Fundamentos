dicionario = {i: i*2 for i in range(10) if i % 2 == 0}
print(dicionario)

dict2 = {f'Item {i}': i**2 for i in range(10) if i % 2 == 0}
print(dict2)
