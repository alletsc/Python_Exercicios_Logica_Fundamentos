# Entendendo argumentos posicionais e nomeados


def fun_name():
    return 'oi'


def anonima(param1, param2): return param1 + param2


class func_class:
    def __call__(self):
        return 'oi'


def soma_posicionais(a, b):
    ''' a e b são posicionais '''
    return a + b


def soma_nomeados(x=5, y=7):
    ''' parametros nomeados recebem valor default'''
    return x + y


def soma_explic_nomeados(*, x=5, y=7):
    ''' o que está depois do * deve ser nomeado'''
    return x + y


def soma_explic_nomeados2(x=5, *, y=7):
    return x + y


def soma_explic_nomeados3(x=5, y=7, /):
    return x + y


def soma_explic_nomeados4(x, y, /, z, *, w):
    return x + y + z + w


print(soma_explic_nomeados(x=10, y=20))
print(soma_explic_nomeados2(1, y=20))
print(soma_explic_nomeados3(1, 3))
print(soma_explic_nomeados4(1, 3, 1, w=3))
