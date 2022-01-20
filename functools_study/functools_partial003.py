from functools import partial

# partial(func, val) -> func2


def exp(x, y):
    print(f'x = {x} , y = {y}')
    return x ** y


# quad = partial(exp, 2) -> aqui x = 2
quad = partial(exp, y=2)
# print(quad(4))

cubo = partial(exp, y=3)
# print(cubo(3))

quart = partial(exp, y=4)
# print(quart(4))

quint = partial(exp, y=5)
# print(quint(5))

# funcoes como argumento

map_soma2 = partial(map, lambda x: x + 2)
# print(list(map_soma2([12, 13, 45, 6])))


def func(x, y, z, a, b, c):
    return x, y, z, a, b, c


a = partial(func, 1, 2, 3)
# print(a(10, 11, 12))

# Exemplo com kwargs (apenas a nivel de curiosidade)


def func2(*args, **kwargs):
    return args, kwargs


b = partial(func2, 1, 2, 3)()
c = partial(func2, 1, 2, 3, b=10)()
# print(a , b)
