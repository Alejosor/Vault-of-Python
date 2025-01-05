# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprímela.
print('Ejercicio #1')
my_tuple = (10, 20, 30, 40, 50)
print(f'{my_tuple}\n')

# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.
print('Ejercicio #2')
my_tuple = (100, 200, 300, 400, 500)
print(f'{my_tuple[1]}\n')

# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.
print('Ejercicio #3')
# my_tuple = (1, 2, 3)
# my_tuple[0] = 10
print("'tuple' object does not support item assignment\n")

# 4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).
print('Ejercicio #4')
my_tuple = (1, 2, 3, 3, 4, 5, 3)
print(f'{my_tuple.count(3)}\n')

# 5. Encuentra el índice de la primera aparición de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").
print('Ejercicio #5')
my_tuple = ("Java", "Python", "JavaScript", "Python")
print(f'El índice de la primera aparición de la cadena "Python" en la tupla es: {my_tuple.index("Python")}\n')

# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.
print('Ejercicio #6')
tuple_one = (1, 2, 3)
tuple_two = (4, 5, 6)
my_tuple = tuple_one + tuple_two
print(f'{my_tuple}\n')

# 7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).
print('Ejercicio #7')
my_tuple = (10, 20, 30, 40, 50)
print(f'{my_tuple[2:4]}\n')

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" 
# y vuelve a convertirla en una tupla. Imprime la tupla resultante.
print('Ejercicio #8')
my_tuple = ("rojo", "verde", "azul")
my_list = list(my_tuple)
my_list[1] = 'amarillo'
my_tuple = tuple(my_list)
print(f'{my_tuple}\n')

# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.
print('Ejercicio #9')
my_tuple = ("rojo", "verde", "azul")
del my_tuple
print("name 'my_tuple' is not defined\n")

# 10. Crea una tupla con un solo elemento (el número 100) e imprímela. 
# Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento.
print('Ejercicio #10')
my_tuple = (100)
print(f'{my_tuple}\n')