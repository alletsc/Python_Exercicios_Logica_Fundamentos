"""
Escreva um programa que armazene informações de livros emprestados por uma biblioteca. Crie um menu que possibilite o usuário:

-verificar os títulos da biblioteca e a situação desses títulos (disponível/emprestado);
-solicitar empréstimo;
-devolver
"""

# Programa personalizado com saida de cores no terminal

emprestado = ['A Branca de Neve', 'Pinóquio',
              'Cinderela', 'Power Rangers', 'Orgulho e Preconceito']

disponivel = ['Barney', 'Os Backyardigans',
              'A Seleção', 'Dom Casmurro', 'Os Miseráveis']


def solicita_emprestimo():
    emprestar = input('Digite o nome do livro que deseja emprestar: ')
    if emprestar in emprestado:
        print('Livro já emprestado')
    else:
        emprestado.append(emprestar)
        disponivel.remove(emprestar)
        print(f'\033[33mLivro emprestado com sucesso\033[m')


def devolver():
    devolver = input('Digite o nome do livro que deseja devolver: ')
    if devolver in disponivel:
        print(f'\033[32mLivro já disponível\033[m')
    else:
        disponivel.append(devolver)
        emprestado.remove(devolver)
        print(f'\033[36mLivro devolvido com sucesso\033[m')


while True:
    print('\033[35m*-*-\033[m' * 10)
    print('\033[35mBem vindo a nossa Biblioteca!\033[m')
    print('\033[35m*-*-\033[m' * 10)

    menu = int(input(("""Selecione uma opção:
    [1] Verificar os títulos da biblioteca e a situação desses títulos;
    [2] Solicitar empréstimo;
    [3] Devolver;
    [4] Sair;
    Digite a opção desejada: """)))

    if menu == 1:
        print(f'\n\033[32;1mNossos Livros: \033[m')
        print(
            f'''\033[33mLivros emprestados:\033[m \n{(', '.join(emprestado))}''')
        print(
            f'''\033[34mLivros disponíveis: \033[m\n{(', '.join(disponivel))}\n''')

    elif menu == 2:
        solicita_emprestimo()
    elif menu == 3:
        devolver()
    elif menu == 4:
        break
    else:
        print("\033[31;4mOpção inválida!\033[m")
        print("\033[31;4mTente Novamente!\033[m \n")
