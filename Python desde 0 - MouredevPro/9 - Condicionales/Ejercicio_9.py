# 1. Escribe un programa que verifique si un número es positivo, negativo o cero.
print("Ejercicio #1")
num = int(input("Ingrese un número:\n"))
if num > 0:
    print("El número es positivo")
elif num < 0:
    print("El número es negativo")
else:
    print("El número es cero")
print("\n")

# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 años o más) o menor de edad.
print("Ejercicio #2")
edad = int(input("Por favor ingresar edad:\n"))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
print("\n")

# # 3. Escribe un programa que verifique si una cadena de texto está vacía y muestre un mensaje en consecuencia.
print("Ejercicio #3")
cadena = input("Introduce una cadena:\n")
if cadena == '':
    print("La cadena esta vacia")
else:
    print("La cadena no está vacía")
print("\n")

# # 4. Crea un programa que solicite dos números al usuario y compare cuál es mayor. Si son iguales, muestra un mensaje indicando la igualdad.
print("Ejercicio #4")
num1 = float(input('Ingrese su 1er número:\n'))
num2 = float(input('Ingrese su 2do número:\n'))

if num1 > num2:
    print(f'Tu primer número {num1} es el mayor de todos')
elif num1 < num2:
    print(f'Tu segundo número {num2} es el mayor de todos')
else:
    print('Ambos números son iguales')
print("\n")

# # 5. Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo.
print("Ejercicio #5")
num_divisible = int(input('Ingrese un número:\n'))
if num_divisible%3 == 0 and num_divisible%5 == 0:
    print("Su número es divisible por 3 y 5")
else:
    print("Su número no es divisible por 3 y 5")
print("\n")

# # 6. Solicita al usuario que ingrese un número y verifica si es par o impar.
print("Ejercicio #6")
num_par_impar = int(input('Ingrese un número:\n'))
if num_par_impar%2 == 0:
    print(f"El número {num_par_impar} es par")
else:
    print(f"El número {num_par_impar} es impar")
print("\n")

# # 7. Escribe un programa que determine si una persona puede votar en función de su edad(mayor o igual a 18). Si tiene 16 o 17 años, indica que puede votar con permiso especial.
print("Ejercicio #7")
edad_voto = int(input("Por favor ingresar edad:\n"))
if edad_voto >= 18:
    print("Puedes votar")
elif edad_voto >=16:
    print("Puedes votar con permiso especial")
else:
    print("Eres menor de edad, no puedes votar")
print("\n")

# # 8. Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida. Si no coincide, muestra un mensaje de error.
print("Ejercicio #8")
contrasena = "12345"
ingreso_user = input("Ingrese su contraseña:\n")
if contrasena == ingreso_user:
    print("Contraseña correcta. Ingresando al sistema")
else:
    print("Contraseña incorrecta")
print("\n")

# # 9. Escribe un programa que determine si un número está entre 10 y 20 (ambos incluidos).
print("Ejercicio #9")
num_entre = int(input("Ingrese un número:\n"))
if 10 <= num_entre <= 20:
    print(f"Su número {num_entre} se encuentra entre 10 y 20")
else:
    print(f"Su número {num_entre} no se encuentra entre 10 y 20")
print("\n")

# # 10. Escribe un programa que simule un semáforo: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.
print("Ejercicio #10")
semaforo = input('Ingrese un color(Rojo, Amarillo o Verde):\n').lower()
if semaforo == 'rojo':
    print("Debe detenerse")
elif semaforo == 'amarillo':
    print("Debe estar alerta")
elif semaforo == 'verde':
    print('Debe avanzar')
else:
    print('Texto no admitido, por favor asegurarse que sea un color valido')
print("\n")