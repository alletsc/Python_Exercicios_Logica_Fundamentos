'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

casa = float(input("Qual o valor da casa que vc deseja comprar? R$ "))
anos = int(input("Digite o numero de anos em que deseja parcelar o seu pagamento: "))
salario = float(input("Qual o seu salário mensal? R$ "))
prestacao = casa /(anos * 12)
minimoParcela = salario * 30 /100

print("Para pagar uma cada de R${:.2f} em {} anos a prestação será de R${:.2f}".format(casa, anos, prestacao))
if minimoParcela >= prestacao:
    print("Empréstimo concedido")
else:
    print("Este valor ultrapassa 30% do seu salário atual. Empréstimo negado.")