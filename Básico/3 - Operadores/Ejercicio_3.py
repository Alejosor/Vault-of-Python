# 1. Realiza las siguientes operaciones aritméticas:
# • Suma: 15 + 25
# • Resta: 50 - 22
# • Multiplicación: 8 * 7
# • División: 100 / 20

suma = 15 + 25
resta = 50 - 22
multiplicacion = 8 * 7
division = 100 / 20
print("Ejercicio #1")
print(f"La suma es ->{suma}")
print(f"La resta es ->{resta}")
print(f"La multiplicación es ->{multiplicacion}")
print(f"La división es ->{division}\n")

# 2. Calcula el resto de la división de 37 entre 5 y almacénalo en una variable remainder. Luego imprímelo.
resto = 37 % 5
print("Ejercicio #2")
print(f"El resto es ->{resto}\n")

# 3. Convierte el número 7 en una cadena de texto y concaténalo con la frase “ es mi número favorito”. Imprime el resultado.
numero = 7
print("Ejercicio #3")
print("Mi número favorito es " + str(numero)+"\n")

# 4. Repite la palabra “Python” 10 veces usando el operador de multiplicación para cadenas y luego imprímela.
print("Ejercicio #4")
print("Python"*10+"\n")

# 5. Crea dos variables: a y b con los valores 12 y 8 respectivamente. Compara si a es mayor que b y almacena el resultado en una variable booleana resultado. Imprime el valor de resultado.
print("Ejercicio #5")
a = 12
b = 8
resultado = a > b
print(f"El resultado de la comparación booleana es {resultado}\n")

# 6. Compara dos cadenas de texto (“apple” y “banana”) usando los operadores > y < y explica cuál tiene mayor orden alfabético.
print("Ejercicio #6")
cadena1 = "apple"
cadena2 = 'banana'
comparacion1 = cadena1 > cadena2
comparacion2 = cadena1 < cadena2
print(f"En la comparación de apple > banana, el resultado es -> {comparacion1}, ya que b esta después de a")
print(f"En la comparación de apple < banana, el resultado es -> {comparacion2}, ya que b esta después de a\n")

# 7. Realiza una comparación lógica usando and para verificar si el número 10 es mayor que 5 y menor que 20. Imprime el resultado.
print("Ejercicio #7")
comparacion3 = 10 > 5 and 10 < 20
print(f"El número 10 es mayor que 5 y menor que 20, llegamos al resultado que es -> {comparacion3}\n")

# 8. Usa el operador or para verificar si el número 7 es menor que 3 o mayor que 5. Imprime el resultado.
print("Ejercicio #8")
comparacion4 = 7 < 3 or 7 > 5
print(f"Al verificar si el número 7 es menor que 3 o mayor que 5, llegamos al resultado que es -> {comparacion3}\n")

# 9. Aplica el operador not para invertir el resultado de la comparación 15 > 20. ¿Cuál es el resultado?
print("Ejercicio #9")
comparacion5 = not(15 > 20)
print(f"Invertimos el resultado de la comparación 15 > 20, llegamos al resultdo invertido que es -> {comparacion5}\n")

# 10. Combina operadores aritméticos y lógicos: Verifica si el número resultante de la expresión (5 * 3) + 2 es mayor que 10 y menor que 20. Imprime el resultado.
print("Ejercicio #10")
valor = (5 * 3) + 2
comparacion6 = valor > 10 and valor < 28
print(f"Verificamos si el número resultante de la expresión (5 * 3) + 2 es mayor que 10 y menor que 20, el resultado termina siendo -> {comparacion6}")
