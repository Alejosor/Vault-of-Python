# 1. Crea una función llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>". Si no se proporciona ningún nombre, debe saludar diciendo "Hola, desconocido".
print('Ejercicio #1')
def personalized_greeting(nombre = 'desconocido'):
    print(f'Hola, {nombre}.\n')
personalized_greeting('Alejo')    
    
# 2. Escribe una función llamada "multiply" que reciba dos números como argumentos y retorne el resultado de multiplicarlos.
print('Ejercicio #2')
def multiply(num1,num2):
    return num1 * num2
print(multiply(5,4),'\n')

# 3. Crea una función llamada "is_even" que reciba un número entero como argumento y retorne True si es par y False si es impar.
print('Ejercicio #3')
def is_even(num):
    if num%2 == 0:
        print(f'El número {num}, es par\n')
    else:
        print(f'El número {num}, es impar\n')
is_even(12)

# 4. Escribe una función llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayúsculas.
print('Ejercicio #4')
def convert_to_uppercase(texto:str):
    print(texto.upper(),'\n')
convert_to_uppercase("hola alejo")

# 5. Crea una función llamada "arbitrary_sum" que reciba un número arbitrario de números como argumentos y retorne la suma de todos ellos.
print('Ejercicio #5')
def arbitrary_sum(*num):
    contador = 0
    for suma in num:
        contador += suma
    print(contador,'\n')
arbitrary_sum(1,2,3,4,5,6,7,8,9)

# 6. Escribe una función llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.
print('Ejercicio #6')
def generate_full_greeting(nombre,apellido):
    print(f'Hola, {nombre} {apellido}\n')

generate_full_greeting(apellido="Soriano",nombre="Alejandro")

# 7. Crea una función llamada "power" que reciba dos números: base y exponente, y retorne el resultado de elevar la base al exponente.
print('Ejercicio #7')
def power(base,exponente):
    result = base ** exponente
    print('El resultado es',result,'\n')
power(2,4)

# 8. Escribe una función llamada "calculate_average" que reciba tres números y retorne su promedio.
print('Ejercicio #8')
def calculate_average(num1,num2,num3):
    promedio = (num1+num2+num3)/3
    print(f"El promedio de los 3 números son: {promedio}\n")
calculate_average(18,17,16)
    
# 9. Crea una función llamada "count_characters" que reciba una cadena de texto y retorne el número de caracteres que contiene.
print('Ejercicio #9')
def count_characters(texto:str):
    num_caracteres = len(texto)
    print(f'La cantidad de caracteres son: {num_caracteres}\n')
count_characters("Alejo es un crack")

# 10. Escribe una función llamada "display_messages" que reciba un número indefinido de cadenas y las imprima en mayúsculas, una por una, tal como se hizo en el archivo proporcionado.
print('Ejercicio #10')
def display_messages(*cadena:str):
    for i in cadena:
        print(i.upper())
display_messages("Alejo","Tiffany","Rosa","Luxo","Daniela",)