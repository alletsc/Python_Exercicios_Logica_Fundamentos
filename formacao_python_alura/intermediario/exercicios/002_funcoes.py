def func():
    return 'Funcao 1'

def func2(funcao):
    return funcao()

x = func2(func)
print(x)

# =======

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome, ):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

y = mestre(saudacao, 'User', saudacao='Boa noite')
print(y)