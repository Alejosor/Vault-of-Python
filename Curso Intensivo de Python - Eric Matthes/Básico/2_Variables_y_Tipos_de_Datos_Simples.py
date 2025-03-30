# VARIABLES Y TIPOS DE DATOS SIMPLES
"""
Esto es una variable...

mi_variable = "información"

Definición:
Podemos decir que una variable es un espacio en memoria que se utiliza para almacenar datos y recuperarlos.
    - Solo pueden contener letras, números y guiones bajos.
    - Pueden empezar por una letra o un guión.
    - No pueden haber espacios debemos emplear, "_" en vez de los espacios.
    - Evitar el uso de palabras clave.

Conviene pensar las variables como etiquetas a las cuales podemos asignar valores. Una variable hace referencia a un valor determinado.

Eliminar espacios en blanco:
Para poder lograr esto, empleamos el método .strip(). Aquí algunos ejemplos:
    palabra = " hola "
    palabra.rstrip() -> "hola "
    palabra.lstrip() -> " hola"
    palabra.strip() -> "hola"

Remover Prefijo:
Para lograr eliminar un prefijo específico si existe al inicio del texto.
    url = "https://google.com"
    limpio = url.removeprefix("https://")  # "google.com"
"""

# Ejercicios
print("EJERCICIOS - VARIABLES")
# 1.	Crea una variable llamada nombre y asígnale tu nombre. Luego imprime su valor.
print("\n*** 1er Ejercicio ***")
nombre = "Alejandro"
print(nombre)

# 2.	Declara dos variables llamadas edad y pais, asígnales valores apropiados y muestra un mensaje que diga: “Hola, soy [nombre], tengo [edad] años y vivo en [pais]”.
print("\n*** 2do Ejercicio ***")
edad = 24
pais = "Perú"
print(f"Hola, soy {nombre}, tengo {edad} años y vivo en {pais}")

# 3.	Crea una variable mensaje que combine texto y una variable ya existente (por ejemplo, nombre) y muéstrala en consola.
print("\n*** 3er Ejercicio ***")
mensaje = "Be that guy"
print(f"Para {nombre}, una de sus frases favorita es: \"{mensaje}\"")

# 4.	Declara una variable curso con el valor "Python" y otra nivel con el valor "básico". Luego imprime: “Estás en el curso de Python nivel básico”.
print("\n*** 4to Ejercicio ***")
curso = "Python"
nivel = "básico"
print(f"Estás en el curso de {curso} nivel {nivel}")

# 5.	Asigna un número entero a una variable numero1 y otro a numero2. Crea una tercera variable suma que almacene la suma de ambos y muestra el resultado.
print("\n*** 5to Ejercicio ***")
numero1 = 50
numero2 = 55
suma = numero1 + numero2
print(f"El resultado de sumar {numero1} + {numero2} es {suma}")

# 6.	Crea una variable precio con valor decimal y una variable cantidad. Luego calcula el total y muéstralo en pantalla.
print("\n*** 6to Ejercicio ***")
precio = 5.70
cantidad = 20
print(f"El resultado del total es {precio*cantidad}")

# 7.	Crea tres variables con nombres válidos y tres con nombres inválidos. Escribe un comentario explicando por qué los inválidos no funcionan.
print("\n*** 7mo Ejercicio ***")
# No funcionaran ya que son palabras reservadas del lenguaje y no se pueden usar para nombrar variables.
# pass = 90
# else = "if"
# import = 'now'

# 8.	Guarda tu color favorito en una variable color_favorito y crea un mensaje que diga: “Mi color favorito es ___”.
print("\n*** 8vo Ejercicio ***")
color_favorito = "Azul"
print(f"Mi color favorito es {color_favorito}")

# 9.	Declara una variable que almacene True o False para indicar si tienes mascotas, y muestra un mensaje que diga: “¿Tienes mascotas? True/False”.
print("\n*** 9no Ejercicio ***")
mascotas = True
print("¿Tienes mascotas?",mascotas)

# 10.	Modifica el valor de una variable después de declararla, y muestra el antes y el después.
print("\n*** 10mo Ejercicio ***")
frase = "Do hard things!"
autor = 'Elon Musk'
autor = 'Casey Neistat'
print(f"El autor de esta frase \"{frase}\" es {autor}")

# 11.	Declara una variable fruta con el valor "   mango   ". Usa strip() para eliminar los espacios y muestra el resultado.
print("\n*** 11vo Ejercicio ***")
fruta = "  mango  "
print(fruta.strip())

# 12.	Crea una variable texto con el valor "***Bienvenido***" y usa strip("*") para eliminar los asteriscos al inicio y final.
print("\n*** 12vo Ejercicio ***")
texto = "***Bienvenido***"
print(texto.strip("*"))

# 13.	Simula un nombre de usuario con espacios y guiones bajos al principio y al final. Usa strip() para limpiar ambos.
print("\n*** 13vo Ejercicio ***")
nombre_user = " _Alejo_ "
print(nombre_user.strip(" _"))

# 14.	Declara una variable url con el valor "https://www.google.com". Usa removeprefix() para eliminar "https://" y "www.", y muestra el resultado.
print("\n*** 14vo Ejercicio ***")
url = "https://www.google.com"
print(url.removeprefix("https://").removeprefix("www."))

# 15.	Tienes un número telefónico "📞+51-987654321". Usa removeprefix() para dejar solo el número sin el ícono ni el código.
print("\n*** 15vo Ejercicio ***")
num_telefonico = "📞+51-987654321"
print(num_telefonico.removeprefix("📞"))

# 16.	Crea una variable altura con el valor "1.75" (como texto). Conviértela a float y muéstrala.
print("\n*** 16vo Ejercicio ***")
altura = "1.75"
print(f"Ahora este número {float(altura)} es de tipo float")

# 17.	Solicita al usuario dos números (usando input()), conviértelos a int, súmalos y muestra el resultado.
print("\n*** 17vo Ejercicio ***")
user_1 = int(input("Ingrese un número por favor:\n"))
user_2 = int(input("Ingrese un número por favor:\n"))
suma = user_1 + user_2
print(f"El resultado de la suma es {suma}")

# 18.	Declara una variable precio_unitario como 3.50 y otra cantidad como 4. Calcula el total usando tipos numéricos adecuados.
print("\n*** 18vo Ejercicio ***")
precio_unitario = 3.50
cantidad = 4
print(f"El total es {precio_unitario*cantidad}")

# 19.	Convierte el texto "2025" a entero y luego súmale 1.
print("\n*** 19vo Ejercicio ***")
texto = "2025"
print(f"El número es {int(texto)+1}")

# 20.	Convierte el número 8.7 a int y explica en un comentario qué sucede con los decimales.
print("\n*** 20vo Ejercicio ***")
num = 8.7
print(f"El número es {int(num)}, aquí el número únicamente toma el valor entero sin redondear")