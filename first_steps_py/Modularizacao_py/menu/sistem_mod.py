def linha(tam = 42):
    return "-" * tam


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


def cab(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cab
    c = 1
    for item in lista:
        print(f' {c} - {item}')
        c += 1
    print(linha())
    opc = leia_int('Sua opção: ')
    return opc
