# 6. Crea un módulo que defina una clase llamada "Car" con propiedades como marca, modelo y año. Importa este módulo en otro archivo y crea una instancia de la clase "Car".

class Car:
    def __init__(self,marca,modelo,año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        
    def presentar(self):
        print(f'Carro:\n- Marca:{self.marca}\n- Modelo:{self.modelo}\n- Año:{self.año}')
