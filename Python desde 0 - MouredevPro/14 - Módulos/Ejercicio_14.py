# # 1. Crea un módulo llamado "calculator" que contenga funciones para sumar, restar, multiplicar y dividir dos números. Importa este módulo en otro archivo y usa sus funciones.
import calculator

# # #Funciones del módulo calculator
try:
    print(f'Suma: {calculator.sumar(3,2)}')
    print(f'Resta: {calculator.sumar(3,2)}')
    print(f'Multiplicación: {calculator.sumar(3,2)}')
    print(f'División: {calculator.sumar(3,2)}')
except ValueError as e:
    print(e)
except Exception as e:
    print(e)

# # 2. Crea un módulo llamado "converter" que tenga funciones para convertir temperaturas entre Celsius y Fahrenheit. Escribe un programa que importe este módulo y realice conversiones.
import converter

# # Funciones del módulo converter
try:
    grado_celsius = int(input('Ingrese la temperatura en Celsius:\n'))
    grado_fahrenheit = int(input('Ingrese la temperatura en Fahrenheit:\n'))
    converter.celsius_to_fahrenheit(grado_celsius)
    converter.fahrenheit_to_celsius(grado_fahrenheit)
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
except Exception as e:
    print(e)

# # 3. Crea un módulo que contenga una lista de nombres de estudiantes y una función que imprima todos los nombres. Importa este módulo en otro archivo y usa la función para mostrar la lista.
import lista_estudiantes
lista_estudiantes.lista_estudiantes()

# # 4. Crea un módulo llamado "geometry" que tenga una función para calcular el área de un círculo y un cuadrado. Usa este módulo en otro archivo para calcular áreas.
import geometry

radio_circulo = 6
lado_cuadrado = 4

geometry.area_circulo(radio_circulo)
geometry.area_cuadrado(lado_cuadrado)

# 5. Escribe un módulo que contenga una función que acepte cualquier número de argumentos y devuelva su suma. Importa y usa la función en otro archivo.
import suma_argumentos

suma_argumentos.suma_argumentos(1,2,3,4,5,6,7,8,9)

# 6. Crea un módulo que defina una clase llamada "Car" con propiedades como marca, modelo y año. Importa este módulo en otro archivo y crea una instancia de la clase "Car".
from garage import Car

carro1 = Car('Lamborghini','Aventador','2014')
carro1.presentar()

# 7. Escribe un módulo que contenga funciones para leer y escribir en archivos de texto. Crea un programa que use estas funciones para escribir y leer datos.
import leer_escribir

# Escribir datos en un archivo
nombre_archivo = 'datos.txt'
contenido = 'Este es un ejemplo de contenido para el archivo.'
leer_escribir.escribir(nombre_archivo, contenido)

# Leer datos del archivo
contenido_leido = leer_escribir.leer(nombre_archivo)
if contenido_leido:
    print(f"Contenido del archivo '{nombre_archivo}':\n{contenido_leido}")

# 8. Crea un módulo llamado "statistics" que tenga funciones para calcular la media y la mediana de una lista de números. Usa este módulo para calcular estos valores en una lista dada.
import statistics

# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Calcular la media
statistics.calcular_media(numeros)

# Calcular la mediana
statistics.calcular_mediana(numeros)

# 9. Crea un módulo que contenga una función para contar cuántas veces aparece una palabra en un texto. Escribe un programa que importe el módulo y lo use para contar palabras en una cadena.
import contar_palabras

# Texto y palabra a buscar
texto = "Este es un ejemplo de texto. Este texto es solo un ejemplo."
palabra = "ejemplo"

# Contar la palabra en el texto
contar_palabras.contador_palabra(palabra, texto)

# 10 Crea un módulo llamado "dates" que contenga funciones para obtener la fecha actual y calcular la diferencia entre dos fechas. Usa este módulo en un programa para mostrar la fecha actual y la diferencia entre dos fechas específicas.
import dates

# Obtener la fecha actual
fecha_actual = dates.obtener_fecha_actual()

# Calcular la diferencia entre dos fechas
fecha1 = "01/01/2022"
fecha2 = fecha_actual.strftime("%d/%m/%Y")
dates.diferencia_fechas(fecha1, fecha2)