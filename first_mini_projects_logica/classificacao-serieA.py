''' Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do Cruzeiro.'''

times  = ( 'Cruzeiro' , 'Palmeiras', 'Santos', 'Grêmio',
         'Corinthians', 'Flamengo', 'Vasco' , 'Chapecoense',
         'Atlético-MG', 'Botafogo', 'Altético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí' , 'Ponte Preta',
         'Atlético-GO')
print("===" * 10)
print("CLASSIFICAÇÃO SÉRIE A 2020")
print("===" * 10)
for t in times:
    print(t)
print("===" * 20)
print(f"Os 5 primeiros colocados são: {times[0:5]}")
print("xxx" * 20)
print(f"Os 4 times na zona de rebaixamento são: {times[-4:]}")
print("xxx" * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print("xxx" * 20)
print(f"O melhor time do Brasil é o Cruzeiro e ele está na {times.index('Cruzeiro')+1}ª posição")
print("xxx" * 10)
