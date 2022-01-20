lista = []
def ordena_num():
    for n in range(0, 3):
        num = float(input('Digite um número: '))
        if n not in lista:
            lista.insert(n, num)
        else:
            print('Número já existe na lista.')
            break
    return sorted(lista, reverse=True)

print(f' Os números em ordem decrescente são: {ordena_num()}')
