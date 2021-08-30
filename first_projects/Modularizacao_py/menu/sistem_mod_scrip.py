import sistem_mod

while True:
    sistem_mod.cab('Título')
    res = sistem_mod.menu(['Opção 1 ', 'Opção 2','Opção 3', 'Sair'])
    if res == 1:
        print(f"001")
    elif res == 2:
        print(f"OPC 02")
    elif res == 3:
        print(f"OPC 03")
    elif res == 4:
        break
    else:
        print('\033[34mERROR!!! Digite uma opção válida.\033[m')
