print( """
      Cardapio:
      100
      1001
      102
      103
      104 """)

menu = 2
total = 0

while menu != 1:
    pedido = int(input("Digite o numero do pedido: "))
    quant = int(input("Digite a quantidade: "))
    if pedido == 100:
        valor = 7.00 * quant
    if pedido == 101:
        valor = 8.50 * quant
    if pedido == 102:
        valor = 10.00 * quant
    if pedido == 103:
        valor = 8.00 * quant
    if pedido == 104:
        valor = 9.30 * quant
    print('Valor a ser pagp por este produto: R$ %.2f' % valor)
    total += valor
    menu = int(input("Digite 2 para continuar ou 1 para finalizar: "))
