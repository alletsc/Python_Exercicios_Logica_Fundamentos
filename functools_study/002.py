from operator import add, mul, sub, floordiv


def add(x, y):
    return x + y


def case_operator(op):
    return {
        '+': add,
        '-': sub,
        '*': mul,
        '/': floordiv
    }[op]


a = case_operator('+')(1, 2)
b = case_operator('/')(6, 5)
print(a)
