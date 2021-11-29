def saudacao(msg, nome):
    print( f'{msg} {nome}! \nSEJA BEM VINDA')

saudacao('Olá', 'Stella')

# -------

def soma3(x, y, z):
    print(x + y + z)

soma3(1, 3, 4)

# -------

def aumento_percentual(valor, percent):
    print(valor + (valor * percent / 100))

aumento_percentual(50, 23)
aumento_percentual(50, 10)

# -----

def fizbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return 'FizzBuzz'
    if x % 5 == 0:
        return 'Buzz'
    if x % 3 == 0:
        return 'Fizz'
    return f'O número foi {x}'

from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    fizbuzz(i)