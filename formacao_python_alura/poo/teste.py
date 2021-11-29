def cria_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo':saldo, 'Limite':limite}
    return conta

def deposita(conta, valor):
    conta['saldo'] += valor 

def saca(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print(f'O seu saldo é de R${ (conta["saldo"])}.')

conta = cria_conta(123, 'Nico', 50.0, 100.0)
deposita(conta, 15)
extrato(conta)