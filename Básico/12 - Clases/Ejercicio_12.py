import math
# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y un método "make_sound" que imprima un sonido genérico.
class Animal:
    def __init__(self, species):
        self.species = species  # Esto es una propiedad

    def make_sound(self):  # Esto es un método
        print("Sonido genérico")

# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacénala en una propiedad pública. Añade el método "make_sound" que imprima un sonido dependiendo de la especie.
class Animal:
    def __init__(self, species):
        self.species = species  # Esto es una propiedad

    def make_sound(self):  # Esto es un método
        if self.species == "Perro":
            print("Guau")
        elif self.species == "Gato":
            print("Miau")
        else:
            print("Sonido genérico")
        
        
# 3. Crea una clase llamada "Car" con las propiedades públicas "brand" y "model". Además, debe tener una propiedad privada "_speed" que inicialmente será 0.
class Car:
    def __init__(self,brand,model):
        self.brand = brand #Propiedad Pública
        self.model = model
        self._speed = 0

# 4. Añade a la clase "Car" un método llamado "accelerate" que aumente la velocidad en 10 unidades. Añade también un método "brake" que reduzca la velocidad en 10 unidades. Asegúrate de que la velocidad no sea negativa.
class Car:
    def __init__(self,brand,model):
        self.brand = brand #Propiedad Pública
        self.model = model
        self._speed = 0
    
    def accelerate(self):
        self._speed += 10
    
    def brake(self):
        if self._speed >=10:
            self._speed -= 10
        else:
            self._speed = 0
    
# 5. Crea una clase "Book" que tenga propiedades como "title" (público) y "author" (privado). Añade un método para obtener el autor y otro para cambiar el título del libro.
class Book:
    def __init__(self,title,author):
        self.title = title
        self._author = author
    
    def get_author(self):
        return self._author
    
    def change_title(self,new_title):
        self.title = new_title

# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. Añade un método para calcular y devolver la nota media del estudiante.
class Estudiante:
    def __init__(self,nombre,apellido,notas):
        self.nombre = nombre
        self.apellido = apellido
        self.notas = list(notas)
    
    def promedio(self):
        contador = 0
        for x in self.notas:
            contador += x
        promedio = contador / len(self.notas)
        return promedio

# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". Añade métodos para depositar y retirar dinero, asegurándote de que no se pueda retirar más de lo que hay en la cuenta.
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def depositar(self,monto):
        if monto > 0:
            self.balance += monto
        else:
            print('No se puede depositar montos negativos')
    
    def retirar(self,monto):
        if monto > 0:
            if monto <= self.balance:
                self.balance -= monto
            else:
                print('Fondos insuficientes')
        else:
            print('No se puede retirar montos negativos')

# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". Añade un método que calcule la distancia entre dos puntos.
class Point:
    def __init__(self,x,y):
        self.y = y
        self.x = x
    
    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((otro_punto.x - self.x) ** 2 + (otro_punto.y - self.y) ** 2)
        return distancia

# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked". Añade un método que calcule el pago total basado en las horas trabajadas y el salario por hora.
class Employee:
    def __init__(self,name,hourly_wage,hours_worked):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
    
    def pago_total(self):
        pago_total = self.hourly_wage * self.hours_worked
        return pago_total
    
    def salario_hora(self):
        return self.hourly_wage

# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). Añade un método para agregar un producto al inventario y otro para mostrar todos los productos disponibles.
class Store:
    def __init__(self,inventory):
        self.inventory = list(inventory)
    
    def agregar_producto(self,producto):
        self.inventory.append(producto)
        return self.inventory
    
    def mostrar_producto(self):
        for producto in self.inventory:
            print(producto)