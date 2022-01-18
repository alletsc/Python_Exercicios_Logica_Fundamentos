'''
HOFs é um conceito que permite a criação de funções que recebem outras funções como argumentos.
'''

# Twice reaplica a função passada como argumento duas vezes.

from typing import Any, Callable

soma = lambda x: x + 2


def reaplica_func(func: Any, arg: Any) -> Any:
    """
        Recebe uma função e um argumento e retorna o resultado da função passada como argumento duas vezes.
    """
    return func(
        func(arg)
    )

# print(reaplica_func(soma, 0))

palavras = ['cachorro', 'coelho', 'elefante', 'amante', 'gato', 'rato']

print(sorted(palavras))

print(sorted(palavras, key=lambda string: string[1]))
print(list(map(lambda val: val * 2, palavras)))
print()
print()

from itertools import groupby

print(list(groupby(palavras, key=lambda string: string[-2:])))
print(list(filter(lambda x: x[-2:] == 'to', palavras)))
