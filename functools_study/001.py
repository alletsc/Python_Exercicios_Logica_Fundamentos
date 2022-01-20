# HOF

def twice(func, val):
    return func(func(val))

def soma2(val):
    return val + 2

x = soma2(1)
y = soma2(3)

z = twice(soma2, 1)








