# 1. Declara una variable text con la frase "Aprendiendo Python" y luego imprime la longitud de la cadena usando len().
text = "Aprendiendo Python"
print(len(text))

# 2. Concatena dos cadenas: "Hola" y "Python", y muestra el resultado en una sola línea.
print("Hola" + " Python")

# 3. Crea una cadena que incluya un salto de línea, y luego imprímela para ver el resultado.
print("Esto es un \nsalto de linea")

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
nombre = "Alejo"
apellido = "Soriano"
edad = 23

print(f"Mi nombre es {nombre}, mi apellido {apellido} y edad es {edad}")

# 5. Desempaqueta los caracteres de la palabra "Python" en variables separadas y luego imprímelos uno por uno.
palabra = "Python"
a,b,c,d,e,f = palabra
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# 6. Extrae un "slice" de la palabra "Programación" para obtener los caracteres desde la posición 3 hasta la 7.
palabra_n = "Programacion"
slice_palabra_n = palabra_n[3:8]
print(slice_palabra_n)

# 7. Invierte la cadena "Python" usando slicing y muestra el resultado.
cadena = "Python"
cadena_slicing = cadena[::-1]
print(cadena_slicing)

# 8. Convierte la cadena "aprendiendo python" en mayúsculas usando el método adecuado e imprímela.
cadena_1 = "aprendiendo python"
print(cadena_1.upper())

# 9. Cuenta cuántas veces aparece la letra "n" en la cadena "Programación en Python".
cadena_2 = "Programación en Python"
print(cadena_2.count("n"))

# 10. Verifica si la cadena "12345" es numérica usando el método adecuado e imprime el resultado.
cadena_3 = "12345"
print(cadena_3.isnumeric())