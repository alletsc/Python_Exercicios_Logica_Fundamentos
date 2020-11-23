'''Refaça o desafio dos triângulos, acrescentando o recurso de mostrar que tipo
 de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''

reta1 = float(input("Digite o valor do primierio segmento da reta: "))
reta2 = float(input("Digite o valor do segundo segmento da reta: "))
reta3 = float(input("Digite o valor do terceirio segmentos da reta: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
    print("Você pode formar um triangulo:")

    if reta1 == reta2 == reta3:
        print("EQUILÁTERO.")

    elif reta1 != reta2 != reta3 and reta1 != reta3:
        print("ESCALENO.")
    else:
        print("ISÓCELES")

else:
    print("Não podemos formar um triangulo.")
    