'''list.append(x): Adiciona um item ao fim da lista.
list.extend(iterable): Adiciona todos os itens do iterável iterable ao fim da lista.
list.insert(i, x): Insere um item em uma dada posição i.
list.remove(x): Remove o primeiro elemento, cujo valor seja x.
list.pop(i): Remove o item de posição i da lista e o retorna. Caso i não seja especificado, retorna o último elemento da lista.
list.clear(): Remove todos os elementos da lista.
list.index(x[, start[, end]]): Retorna o índice do primeiro elemento cujo valor seja x.
list.count(x): Retorna o número de vezes que o valor x aparece na lista.
list.sort(key=None, reverse=False): Ordena os items da lista (os argumentos podem ser usados para customizar a ordenação).
list.reverse(): Reverte os elementos da lista.
list.copy(): Retorna uma lista com a cópia dos elementos da lista de origem.'''
'''
lista = [1, 2, 3, 4, 5]
lista.pop()
print(lista)
lista.append(7)
print(lista)
'''


db = [i * 2 for i in range(0, 10)]
db2 = [x ** 2 for x in range(11)]
print(db2)
print(db)


db3 = []
for i in range(0, 10):
    db3.append(i * 2)

print(db3)
