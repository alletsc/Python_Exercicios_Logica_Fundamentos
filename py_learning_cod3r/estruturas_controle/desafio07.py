from typing import Pattern


PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}
textos = ['João gosta de futebol e política',
          'A praia foi divertida', ]

for p in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(p.lower().split()))
    if intersecao:
        print(f"Encontramos as palavras proibidas: {intersecao}")
    else:
        print(f'Texto aprovado')
