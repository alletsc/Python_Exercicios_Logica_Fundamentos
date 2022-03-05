
# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma
# lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da
# média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro,
# . . . ).

temperatura = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
media = 0
acima_media = {}
for i in range(len(meses)):
    temperatura.append(
        float(input('Informe a Temperatura media de ' + meses[i] + ':\n')))

media += temperatura[i]
media = media/len(meses)

for i in range(len(meses)):
    if(temperatura[i] > media):
        acima_media.update({meses[i]: temperatura[i]})

print(acima_media)
