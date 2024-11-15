# 1. Imprime "¡Hola Mundo!" por consola.
print("Hola Mundo")

# 2. Escribe un comentario de una sola línea explicando qué hace el código del Ejercicio 1.
# Lo que hace la sentencia print(), es imprimir en consola lo que declaremos dentro de los parentesis.

# 3. Imprime tu nombre y edad en la misma línea utilizando la función print.
print("Nombre: Alejandro - Edad: 23 años")

# 4. Usa la función type() para imprimir el tipo de dato de una cadena de texto, un número entero y un número decimal.
print(type("Texto"))
print(type(24))
print(type(3.14))

# 5. Escribe un comentario en varias líneas explicando qué son los tipos de datos en Python.
'''
Los tipos de datos, son la clasificación
de valores de datos similares que dependiendo el tipo de valor
que sean se les dará una categoría.
'''

# 6. Imprime el resultado de concatenar dos cadenas de texto, por ejemplo: "Hola" y "Mundo".
print("Hola" + "Mundo")

# 7. Crea una variable para almacenar tu nombre, otra para tu edad, e imprime ambas en la misma línea.
nombre = "Alejandro"
edad = 23

print(f"Me llamo {nombre} y tengo {edad} años")

# 8. Escribe un programa que solicite al usuario su nombre y lo imprima junto con un saludo.
nombre_usuario = input("Por favor ingrese su nombre: \n")
print(f"Te damos la bienvenida al curso {nombre_usuario}")

# 9. Usa print() para mostrar el resultado de la suma de dos números enteros y el tipo de dato resultante.
resultado = 10 + 20
print(f"El resultado es {resultado} y el tipo de dato es", type(resultado))

# 10. Comenta el código del Ejercicio 9, y explica qué hace cada línea usando comentarios de una sola línea.
#En una varaible almacenamos la suma de los números enteros 10 y 20, en la siguiente se imprime la suma de los números y en la última el tipo de dato que es la suma