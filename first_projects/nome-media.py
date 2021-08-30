'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''

aluno = {}
aluno['nome'] = str(input("Digite o nome do aluno: "))
aluno['media']= float(input(f"Digite a media de {aluno['nome']}: "))
if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
    print(f"Parabens {aluno['nome']}, vc foi aprovado.")
elif aluno['media'] >= 5 and aluno['media'] < 7:
    aluno['situacao'] = 'recuperacao'
    print(f"{aluno['nome']} vc está de recuperação. Estude mais.")
else:
    aluno['situacao'] = 'reprovado'
    print(f"Sinto muito {aluno['nome']} vc está reprovado.")
for k,  v in aluno.items():
    print(f"\n{k} é igual a {v}")
print()