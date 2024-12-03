# 1. Crea una lista con los números del 1 al 5 e imprímela.
print('Ejercicio #1')
numbers = [1,2,3,4,5]
print(f'{numbers}\n')

# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].
print('Ejercicio #2')
numbers_dos_cifras = [10, 20, 30, 40, 50]
print(f'{numbers_dos_cifras[2]}\n')

# 3. Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] e imprímela.
print('Ejercicio #3')
numbers.append(6)
print(f'{numbers}\n')

# 4. Inserta el número 15 en la posición 2 de la lista [10, 20, 30, 40, 50].
print('Ejercicio #4')
numbers_dos_cifras.insert(2,15)
print(f'{numbers_dos_cifras}\n')

# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].
print('Ejercicio #5')
numbers_dos_cifras = [10, 20, 30, 40, 50]
numbers_dos_cifras.remove(30)
print(f'{numbers_dos_cifras}\n')

# 6. Usa la función pop() para eliminar el último elemento de la lista [1, 2, 3, 4, 5] 
# y almacénalo en una variable. Imprime la variable y la lista.
print('Ejercicio #6')
numbers = [1,2,3,4,5]
num_eliminado = numbers.pop()
print(f'{num_eliminado}\n')

# 7. Invierte la lista [100, 200, 300, 400, 500] e imprímela.
print('Ejercicio #7')
numbers_tres_cifras = [100, 200, 300, 400, 500]
numbers_tres_cifras.reverse()
print(f'{numbers_tres_cifras}\n')

# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprímela.
print('Ejercicio #8')
numbers = [3, 1, 4, 2, 5]
numbers.sort()
print(f'{numbers}\n')

# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. 
# Imprime la lista resultante.
print('Ejercicio #9')
list_a = [1, 2, 3]
list_b = [4, 5, 6]
new_list = list_a + list_b
print(f'{new_list}\n')

# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] 
# que van desde la posición 1 hasta la 3 (sin incluir la posición 3).
print('Ejercicio #10')
numbers_dos_cifras = [10, 20, 30, 40, 50]
new_list=numbers_dos_cifras[1:3]
print(f'{new_list}\n')