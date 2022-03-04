from decimal import Decimal

area = float(input('Digite a área a ser pintada em metros quadrados: '))

# def calcula_lata(area):
litros = area / 3
latas = Decimal(litros / 18)
preco = latas * 80

print(f'Serão necessárias {round(latas)} latas de tinta. O valor a ser pago é de R${preco:.2f}')
