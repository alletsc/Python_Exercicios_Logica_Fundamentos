''' Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
1 - o primeiro que indique o número a calcular e
2 - outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial'''

def fat (n, show=False):
    """
    >>> Calcula o fatorial de um numero.
    num = numero a ser calculado
    show  = opcional, mostra ou nao a conta
    return = O fatorial de num

    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

num = (int(input('Digite um numero: ')))
print(fat(num, show=True))
print()
help(fat)
