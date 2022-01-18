from typing import NewType

Radiano = NewType('Radiano', int)


def soma(a, b):
    # PEP257 pydocstyle
    """ Retorna a soma de dois números.

        :args a: objeto somável 1
        :args b: objeto somável 2

        :return: soma dos dois objetos
    """
    return a + b
