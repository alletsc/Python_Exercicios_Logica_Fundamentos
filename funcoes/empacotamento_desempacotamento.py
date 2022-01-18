
def my_sum(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o):
    return a + b + c + d + e + f + g + h + i + j + k + l + m + n + o

print(my_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))

def my_sum2(*arg):
    '''Só lida com args posicionais e resultam em um tuple'''
    print(arg)
    print(type(arg))
    print(sum(arg))


def my_sum3(*arg, **kwargs):
    '''Kwargs lida com args nomeados e resultam em um dict'''
    print(arg)
    print(f' *: {type(arg)}')
    print(kwargs)
    print(f' **: {type(kwargs)}')
    print(sum(arg))

my_sum3(1, 2, 3, 4, 5, a = 11, b = 12)

lista = [-2, 2, 3, 4, 90, -68]

def my_min(*lista):
    return min(lista)

print(my_min(*lista))
