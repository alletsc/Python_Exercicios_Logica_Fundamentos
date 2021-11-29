def func(*args):
    print(args)

var = func(1,3,4,6,7,9,0)

# ==========

lista = [1,2,3,4,5]
n1, n2, *n = lista
print(n1, n2, lista)

# ==========

var = 'Variável'

def func():
    print(var)
func()