from operator import add, mul
from functools import partial, reduce

soma = partial(add, 2)
print(soma(3))

print(reduce(add, [1, 2, 3, 4, 5]))
print(reduce(mul, [1, 2, 3, 4, 5]))

soma2 = partial(reduce, add)
mul2 = partial(reduce, mul)

