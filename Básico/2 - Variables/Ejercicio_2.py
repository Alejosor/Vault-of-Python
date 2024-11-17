# 1. Declara y asigna valores a las siguientes variables:
# • name: una cadena que contenga tu nombre.
name = "Alejandro"
# • age: un número entero que represente tu edad.
edad = 23
# • height: un número flotante que represente tu altura.
altura = 1.82
# • Imprime cada variable en una línea separada.
print(name)
print(edad)
print(altura)

# 2. Convierte la variable age de entero a cadena y concaténala con un texto que diga cuántos años tienes.
print("Tengo ", str(edad), "años.")

# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False según corresponda e imprímela.
is_student : bool = True
print(f"Estado Estudiante Activo: {is_student}")

# 4. Usa la función len() para calcular cuántos caracteres tiene tu nombre completo, almacenado en una variable.
fullName = "AlejandroGabrielSorianoPalomino"
print("Los cantidad de caracteres de mi nombre completo son: ",len(fullName))

# 5. Declara tres variables en una sola línea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.
nombre, apellido, ciudad_de_origen = "Alejandro", "Soriano", "Lima"
print(nombre,apellido,ciudad_de_origen)

# 6. Usa la función input() para solicitar al usuario su color favorito y almacénalo en una variable color. Luego, imprime el valor ingresado.
color = input("Ingrese su color favorito por favor: ")
print(color)

# 7. Declara una variable fruit e inicialízala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.
fruit = "Naranja"
print(fruit)
fruit = "Melón"
print(fruit)

# 8. Convierte un número decimal, almacenado en la variable price, a un número entero y luego imprímelo.
price = int(3.99)
print("Este es el número decimal en la variable precio: ",price,", pero ahora es de tipo -> ", type(price))

# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una dirección usando la función len(). Imprime el resultado.
address_len = len("Esta es la dirección")
print("La cantida de caracteres en la variable address_len es de: ", address_len)

# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurándote de que siempre será un número. Luego, cambia su valor a un número diferente y verifica el tipo de la variable con type().
phone : int = 987654321
phone = 912345678
print(type(phone))