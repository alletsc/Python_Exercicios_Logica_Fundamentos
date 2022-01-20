sinal= int(input('''Digite o valor correspondente ao sinal:
[1] - Verde
[2] - Amarelo
[3] - Vermelho '''))

if sinal == 1:
  print("Pode passar")
elif sinal == 3:
  print("Pare")
elif sinal == 2:
    print('Aguarde')
else:
    print('Valor inválido')

