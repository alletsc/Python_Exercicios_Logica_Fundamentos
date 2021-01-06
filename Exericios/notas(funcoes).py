def notas(*n, sit=False):
    """
    -> Função para analisar notas de alunos.
    parametro n: uma ou mais notas
    parametor sit: opcional, se deve ou nao adicionar situação
    return: dicionario
    """
    r = dict()
    r ['total'] = len(n)
    r ['maior'] = max(n)
    r ['menor'] = min(n)
    r ['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            print("APROVADO")
        elif r['média'] >= 5:
            print("RECUPERAÇÃO")
        else:
            print("RERPOVADO")
    return r
res = notas(5.5, 9, 6, sit=True)
print(res)
help(notas)
