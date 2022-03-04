def soma(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b


try:
    n1 = float(input("Digite um num: "))
    n2 = float(input("Digite outro num: "))

    operacao = input('''
    [1] - soma
    [2] - subtração
    [3] - multiplicação
    [4] - divisão
    Digite a opção correspondente: ''')
except (ValueError):
    print('''
        Por favor digite apenas números.
        Fim do programa.
        Execute novamente para continuar.''')
else:
    if operacao == '1':
        print(f'{n1} + {n2} = {soma(n1, n2)}')
    elif operacao == '2':
        print(f'{n1} - {n2} = {sub(n1, n2)}')
    elif operacao == '3':
        print(f'{n1} * {n2} = {mult(n1, n2)}')
    elif operacao == '4' and n2 != 0:
        print(f'{n1} / {n2} = {div(n1, n2)}')
    elif operacao == '4' and n2 == 0:
        print('Não é possível dividir por 0.')
    else:
        print('Operação inválida. Tente novamente.')
print('Fim do programa.')
