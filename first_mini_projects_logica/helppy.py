c = ('\033[m',       #sem cor
     '\033[0;30;41m',#vermelho
     '\033[0;30;42', #verde
     '\033[0;30;43', #amarelo
     '\033[0;30;44', #azul
     '\033[0;30;45', #roxo
     '\033[0;30;46', #branco
     );

def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam  = len(msg) + 4
    print(c[cor], end='')
    print("~" * tam)
    print(f'  {msg}  ')
    print("~" * tam)
    print(c[0], end='')


comando =''
while True:
    titulo("AJUDA PYHELP", 2)
    comando = str(input("Função ou biblioteca > "))
    if comando.upper() == "FIM":
         break
    else:
        ajuda(comando)
titulo("ATÉ LOGO", 1)