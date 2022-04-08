# Crie um programa que solicite 10 notas de alunos de uma turma de programação computacional e ao final imprima todas as notas e a média da turma. Deve-se usar o comando while

alunos = []

while True:
    for i in range(10):
        nota = float(input(f'Digite a nota do aluno {i+1}: '))
        alunos.append(nota)
        media = sum(alunos) / len(alunos)
    print(f"As notas digitadas foram: \n\t{alunos}")
    print(f'A média da turma é {media:.2f}')
    print('Obrigada por utilizar o nosso programa. Volte sempre!')
    break

