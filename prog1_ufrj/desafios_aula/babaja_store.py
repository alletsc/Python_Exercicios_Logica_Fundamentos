#Controle de qualidade das peças da equipe Ali-Babaja

limSup= 11.05
limInf= 10.95

try:
    while True:
      print('Para sair digite "sair".')
      peca = float(input("Digite a dimensão da peça: "))
      if limSup >= peca and limInf <= peca:
        print("Peça dentro dos limites de tolerância.")
      else:
        print("Peça fora dos limites de tolerância! Refaça a peça.")

except ValueError:
     print("Saindo do programa...")
