# 1. Declara una variable quote con la frase: "El aprendizaje de Python es divertido".
# Convierte todas las letras en minúsculas y luego imprímela.
quote = "El aprendizaje de Python es divertido"
print(quote.lower())

# 2. Crea una cadena con tu comida favorita en formato de lista separada por comas 
# (ejemplo: "pizza, hamburguesa, sushi") y divídela en elementos usando el método split().
lista_comida = "pizza,hamburguesa,sushi"
comida = lista_comida.split(",")
print(comida)

# 3. Usa la función join() para combinar una lista de palabras ["Python", "es", "asombroso"] 
# en una sola cadena separada por espacios.
lista_palabras = ["Python","es","asombroso"]
cadena = "-".join(lista_palabras)
print(cadena)

# 4. Declara una cadena con la frase "La programación requiere paciencia" y 
# reemplaza la palabra "paciencia" por "dedicación". Imprime el resultado.
frase = "La programación requiere paciencia"
print(frase.replace("paciencia","dedicación"))

# 5. Comprueba si la palabra "Python" está contenida en la frase "Estoy aprendiendo Python" 
# usando el operador in, e imprime el resultado.
frase_1 = "Estoy aprendiendo Python"
print("Python" in frase_1)

# 6. Declara una variable con un nombre en minúsculas (ejemplo: "juan perez") y 
# usa métodos de cadena para convertirla en formato de título ("Juan Perez").
nombre = "juan perez"
print(nombre.title())

# 7. Declara una cadena con espacios extra al principio y al final (ejemplo: "   Python   ") 
# y elimina los espacios innecesarios usando el método adecuado.
cadena_1 = "   Python   "
print(cadena_1.replace(" ",""))

# 8. Escribe una cadena de texto que incluya tanto comillas dobles como simples 
# (ejemplo: 'Ella dijo: "Estoy aprendiendo Python"') y luego imprímela.
print("'Ella dijo:\"Estoy aprendiendo Python\"'")

# 9. Verifica si la cadena "Hola123" contiene únicamente caracteres alfabéticos 
# usando el método adecuado. Imprime el resultado.
cadena_2 = "Hola123"
print(cadena_2.isalpha())

# 10. Divide la frase "Python es fácil y poderoso" en dos partes: 
# desde el inicio hasta la palabra "fácil", y desde "fácil" hasta el final, usando slicing. 
# Imprime ambas partes.
frase_2 = "Python es fácil y poderoso"
frase_2_slice1 = frase_2[0:16]
frase_2_slice2 = frase_2[10:]
print(frase_2_slice1)
print(frase_2_slice2)