from math import pi
import sys


def circle(radius):
    return pi * float(radius) ** 2


if __name__ == '__main__':
    raio = float(input('Enter the radius: '))
    area = circle(raio)
    print(f'The area of ​​the circle is = {area:.2f}')
