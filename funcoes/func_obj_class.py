""" Funcoes como objetos de primeira classe"""
from typing import Callable, Dict

'''
calc: Dict[str, Callable] = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}
'''

# print(calc['soma'](2, 3))
# print(calc['subtracao'](1, 1))


def soma2(a, b):
    return a + b


def subtracao2(a, b):
    return a - b


def multiplicacao2(a, b):
    return a * b


def divisao2(a, b):
    return a / b


calc_named = {
    'soma': soma2,
    'subtracao': subtracao2,
    'multiplicacao': multiplicacao2,
    'divisao': divisao2
}

somas = [
    lambda x: x + 0,
    lambda x: x + 1,
    lambda x: x + 2
]
