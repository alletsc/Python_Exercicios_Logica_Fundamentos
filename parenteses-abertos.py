'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

expr = str(input("Digite sua expressão: "))
listexpr = list()
for c in expr:
    if c == '(':
        listexpr.append('(')
    elif c == ')':
        listexpr.append(')')
        if len(listexpr) > 0:
            listexpr.pop()
        else:
            lisexpr.append(')')
            break
if len(listexpr) == 0:
    print('Expressão OK')
else:
    print('Verifique sua expressão.')
    