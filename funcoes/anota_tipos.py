def soma(x: int, y: int) -> int:
    return x + y

# print(soma(1, 2))
# print(soma('a', 'b'))
# print(soma('12', 'b'))
# print(soma(1, 'b'))

from numbers import Number
from typing import Union, Any, List, Dict, #Sequence

# n_tipos = Union(Number, list, str)

# def sub(x: n_tipos, y: n_tipos) -> n_tipos:
    # return x - y


def identidade(val: Any) -> Any:
    return val

def sum2(lista: List) -> int:
    return sum(lista)


def cadastro_user(nome: str,
                  idade: int,
                  email: str) -> Dict[str, Union[str, int, List[str]]]:
    return {'nome': nome,
            'idade': idade,
            'email': email}

print(cadastro_user('João', 32, ['joao@email.com', 'jao@email2.com']))

# def min(seq: Sequence):
    # return min(seq)


