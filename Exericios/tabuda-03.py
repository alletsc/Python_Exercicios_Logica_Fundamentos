''' Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
 O programa será interrompido quando o número solicitado for negativo.'''
 

print("---" * 10)
print("TABUADA DE NUMERO POSITIVOS")
print("---" * 10)
while True:
    n = int(input("Digite um número para ver a sua tabuada: "))
    print("---" * 10)
    if n < 0:
        break
    for c in range (1,11):
        print(f"{n} x {c} = {n*c} ")
    print("---" * 10)
print("Apenas numeros positivos. Reinicie o programa para continuar.")