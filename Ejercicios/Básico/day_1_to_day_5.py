# Ejercicios de Python

# -------------------------------------------
# 1. Hola Mundo
# -------------------------------------------
# 1.1 Escribe un programa que imprima en la consola:
# - Tu nombre.
# - Tu edad.
# - Un mensaje motivacional.
print('\n1. Hola Mundo')
print('Nombre: Alejosor')
print('Edad:',23)
print('Mensaje motivacional: "Do More, Do hard things"\n')

# -------------------------------------------
# 2. Variables
# -------------------------------------------
# 2.1 Declara tres variables con los siguientes valores: tu nombre, tu edad y tu ciudad.
# 2.2 Imprime una frase utilizando esas variables en el siguiente formato:
# "Mi nombre es [nombre], tengo [edad] años y vivo en [ciudad]."
# 2.3 Intercambia los valores de dos variables sin declarar una nueva variable auxiliar.
print('2. Variables')
nombre, edad, ciudad = 'Alejosor', 23, 'Chiclayo'
print(f'Mi nombre es {nombre}, tengo {edad} años y vivo en {ciudad}.')

a, b = 1, 2
print(f'Los valores son: a = {a} y b = {b}')
a, b = b, a
print(f'Los nuevos valores son: a = {a} y b = {b}\n')

# -------------------------------------------
# 3. Operadores
# -------------------------------------------
# 3.1 Calcula el resultado de las siguientes expresiones y explica por qué se obtiene ese resultado:
# - 5 + 2 * 3
# - (5 + 2) * 3
# - 10 / 3
# - 10 // 3
# - 2 ** 3
# print('3. Operadores')
# print('Ejercicio #1:',(5 + 2 * 3))
# print('Ejercicio #2:',((5 + 2) * 3))
# print('Ejercicio #3:',(10 / 3))
# print('Ejercicio #4:',(10 // 3))
# print('Ejercicio #5:',(2 ** 3),'\n')

# 3.2 Escribe un programa que pida dos números al usuario y realice las operaciones básicas (suma, resta, multiplicación y división) con ellos.
# num1=float(input('Ingrese su 1er número:\n'))
# num2=float(input('Ingrese su 2do número:\n'))

# print(f'Sus números son: {num1} y {num2}')
# print('Suma:',(num1+num2))
# print('Resta:',(num1-num2))
# print('Multiplicación:',(num1*num2))
# if num2 == 0:
#     print('Error no se puede dividir')
# else:
#     print('División:',(num1/num2),'\n')

# -------------------------------------------
# 4. Strings
# -------------------------------------------
# 4.1 Crea un programa que solicite al usuario un texto y:
# - Lo convierta a mayúsculas.
# - Reemplace todas las vocales por un '*'.
# - Imprima el texto en reversa.
# print('4. Strings')
# texto = input('Ingrese un texto:\n')
#versión 1
# texto = texto.upper()
# texto = texto.replace("A","*")
# texto = texto.replace("E","*")
# texto = texto.replace("I","*")
# texto = texto.replace("O","*")
# texto = texto.replace("U","*")
# print(texto[::-1],'\n')

#versión 2
# vocales = ['a','e','i','o','u','A','E','I','O','U']
# for i in vocales:
#     texto = texto.upper()
#     vocal = str(i)
#     if texto.find(vocal):
#         texto = texto.replace(vocal,'*')
# print(texto, '\n)

# 4.2 Pide al usuario su nombre completo y descompónlo en nombre y apellidos usando split(). Imprime cada parte por separado.
# nombre_completo = input("Ingrese su nombre completo:\n")
# palabras = nombre_completo.split()
# print(palabras)
# print(palabras[0])
# print(palabras[1])

# 4.3 Escribe un programa que cuente cuántas veces aparece la letra "a" en un texto dado por el usuario.
# texto_user = input('Ingrese un texto:\n')
# cuenta_a = texto_user.count('a')
# print(f'El caracter "a" sale {cuenta_a} veces')

# -------------------------------------------
# 5. Listas
# -------------------------------------------
# 5.1 Crea una lista con los nombres de tus tres comidas favoritas. Luego:
# comidas_favoritas = ['pizza','ceviche','pie de manzana']
# print(comidas_favoritas)
# # - Agrega una comida más al final.
# comidas_favoritas.append('arroz chaufa')
# print(comidas_favoritas)
# # - Inserta una comida al inicio.
# comidas_favoritas.insert(0,'monstrito')
# print(comidas_favoritas)
# # - Elimina la segunda comida de la lista.
# comidas_favoritas.pop(1)
# print(comidas_favoritas)
# # - Imprime la lista final.
# print(comidas_favoritas,'\n')

# 5.2 Escribe un programa que pida al usuario cinco números, los almacene en una lista, y luego:
user_numbers=[]
for i in range(0,5):
    user_numbers.append(input('Ingrese un número:\n'))
print(user_numbers)

# - Imprima la lista en orden inverso.
user_numbers.reverse()
print(user_numbers)

# - Calcule la suma y el promedio de los números.
suma = 0
for i in user_numbers:
    num = int(i)
    suma += num

promedio = suma/(len(user_numbers))
print(f'La suma de los números es {suma}')
print(f'El promedio de los números es {promedio}')  

# - Encuentre el número mayor y el menor.
mayor = menor = int(user_numbers[0])

for i in user_numbers:
    num = int(i)
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num

print(f'El menor de los números es {menor}')
print(f'El mayor de los números es {mayor}')