
with open('pessoas.csv') as arquivo:  # abir pessoa
    with open('pessoas.txt', 'w') as saida:  # abrir pessoa txt
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('Arquivo fechado')

if saida.closed:
    print('Saida arq fechado')
