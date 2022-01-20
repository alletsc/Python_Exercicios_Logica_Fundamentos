''' Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)'''

print('---' * 10)
print()
def leia_int(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[0;31mERROR!!! Digite um numero inteiro valido.\033[m")
        if ok:
            break
    return valor


n = leia_int('Digite um numero: ')
print(f'Vc digitou o numero {n}')
print('---' * 10)
print()

