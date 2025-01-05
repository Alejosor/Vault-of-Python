# 4. Crea un módulo llamado "geometry" que tenga una función para calcular el área de un círculo y un cuadrado. Usa este módulo en otro archivo para calcular áreas.
from math import pi as PI
def area_circulo(radio):
    circulo = PI*(radio**2)
    print(f'El área del circulo es {circulo}')

def area_cuadrado(lado):
    cuadrado = lado ** 2
    print(f'El área de un cuadrado es {cuadrado}')