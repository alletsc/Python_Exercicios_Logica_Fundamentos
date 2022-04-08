'''Faça um programa que calcule o número médio de alunos por turma.
Para isto peça a quantidade de turmas e a quantidade de alunos para cada turma
obs.: As turmas não podem ter mais de 40 alunos.'''


def media_alunos_turma():
    num_turmas = int(input('Digite o número de turmas: '))
    total_alunos = 0
    for i in range(num_turmas):
        num_alunos = int(input(f'Digite o número de alunos da turma {i+1}: '))
        if num_alunos > 40 or num_alunos < 0:
            print('Número de alunos inválido! \nPor favor cheque a quantidade de alunos e reinicie o programa.')
            break
        else:
            total_alunos += num_alunos
            print(f"O número total de alunos é {total_alunos}")
            media_alunos = total_alunos / num_turmas
            print(f"A média de alunos por turma é {media_alunos:.2f}")

media_alunos_turma()

