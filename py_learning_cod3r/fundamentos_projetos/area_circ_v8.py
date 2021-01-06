from math import pi


def circulo(raio):
    print(f'Área do circulo = ', pi * float(raio) ** 2)


if __name__ == '__main__':
    raio = float(input('Digite o raio: '))
    circulo(raio)
