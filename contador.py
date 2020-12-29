n = 1
par = impar = 0
while n !=0:
    n = int(input("Digite um numero (para sair digite 0): "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("Voce digitou {} números pares.".format(par))
print("Voce digitou {} números impares.".format(impar))
