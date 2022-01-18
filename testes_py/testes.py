""" Calculadora para exemplos com testes sem framework """

def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

#testes com assert (verificação)

assert soma(5, 5) == 10

assert sub(5, 5) == -1, f'Erro na subtração {sub(5, 5)}'

assert mul(5, 5) == 25

assert div(5, 5) == 1
