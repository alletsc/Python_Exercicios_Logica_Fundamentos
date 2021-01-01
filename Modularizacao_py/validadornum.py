def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERROR! Por favor digite um valor válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\n\033[34m Usuário interrompeu o programa. \033[m')
            return 0
        else:
            return n

def leia_float(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERROR! Por favor digite um valor válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\n\033[34m Usuário interrompeu o programa. \033[m')
            return 0
        else:
            return n

num_int= leia_int("Digite um num inteiro: ")
num_float = leia_float("Digite um numero real: ")
print(f'Valor inteiro: {num_int} \nValor real: {num_float}')