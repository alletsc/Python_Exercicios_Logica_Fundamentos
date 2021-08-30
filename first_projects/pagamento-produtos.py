''' Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal
 e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros'''
print('{:=^40}'.format("LOJA STELLAR"))

valor = float(input("Digite o valor a ser pago: R$"))
print('''Escolha a condição de pagamento:
[1] pagamento á vista, em dinheiro 
[2] à vista no cartão, no cartão
[3] 3x ou mais no cartão 
[4] Preço formal \n''')
opcao = int(input("Digite a sua opção: "))
print("Você escolheu a opção {}".format(opcao))

if opcao == 1:
    total1 = valor - ((valor * 10) / 100)
    print("Você deve pagar {}".format(total1))
elif opcao == 2:
    total2 = valor - ((valor * 5) / 100)
    print("Você deve pagar {}".format(total2))
elif opcao == 3:
    total3 = valor + ((valor * 20) / 100)
    print("Você deve pagar {}".format(total3))
elif opcao == 4:

    print("Você deve pagar {}".format(valor))
else:
    print("Por favor escolha uma opção valida de pagamento.")
    