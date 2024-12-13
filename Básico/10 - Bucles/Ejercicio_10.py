# 1. Usa un bucle while para imprimir los números del 1 al 10.
print("Ejercicio #1")
num = 1
while num <= 10:
    print(num)
    num += 1
print('\n')

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada número.
print("Ejercicio #2")
my_list = [10, 20, 30, 40, 50]
for i in my_list:
    print(f"El número de la lista: {i}")
print('\n')

# 3. Escribe un programa que use un bucle while para sumar los números del 1 al 100 e imprime el resultado.
print("Ejercicio #3")
num1_to_num100 = 0
contador = 1
while contador <= 100:
    num1_to_num100 += contador
    contador += 1
print(f'La suma de los números del 1 al 100 es {num1_to_num100}') 
print('\n')

# 4. Escribe un bucle for que imprima cada carácter de la cadena "Python".
print("Ejercicio #4")
cadena = 'Python'
for i in cadena:
    print(i)
print('\n')

# 5. Usa un bucle while para encontrar el primer número divisible por 7 entre 1 y 50.
print("Ejercicio #5")
x = 1
while x <= 50:
    if x%7==0:
        print(f'El primer número divisible por 7 entre 1 y 50 es: {x}')
        break
    x+=1
print('\n')

# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.
print("Ejercicio #6")
my_dict = {"name": "Brais", "age": 37, "country": "Galicia"}
for i in my_dict:
    print(i)
print('\n')

# 7. Escribe un programa que use un bucle while para imprimir los números pares entre 1 y 20.
print("Ejercicio #7")
y = 1
while y <= 20:
    if y%2==0:
        print(f'Este es un número par entre 1 y 20: {y}')
    y += 1
print('\n')

# 8. Usa un bucle for con la función range() para imprimir los números del 1 al 10 en orden inverso.
print("Ejercicio #8")
for i in reversed(range(1,11)):
    print(i)
print('\n')

# 9. Escribe un programa que use un bucle for para contar cuántas veces aparece el número 30 en la lista[30, 10, 30, 20, 30, 40].
print("Ejercicio #9")
my_list = [30, 10, 30, 20, 30, 40]
contador = 0 
for i in my_list:
    if i == 30:
        contador += 1
print(f'El número 30 sale la sigiente cantidad de veces: {contador}')
print('\n')

# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".
print("Ejercicio #10")
nombres = [ "Alejandro", "Luis", "Carla", "Sofía", "Mateo", "Brais", "Valeria", "Javier", "Ana", "Marcos"]
for i in nombres:
    print(i)
    if i == "Brais":
        print("Se encontró el nombre Brais")
        break
print("Programa terminado")