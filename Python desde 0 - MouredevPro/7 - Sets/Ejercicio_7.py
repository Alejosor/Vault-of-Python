# 1. Crea un set con los números del 1 al 5 e imprímelo.
print('Ejercicio #1')
my_set = {1, 2, 3, 4, 5}
print(f'{my_set}\n')

# 2. Añade el número 6 al set {1, 2, 3, 4, 5} e imprímelo.
print('Ejercicio #2')
my_set.add(6)
print(f'{my_set}\n')

# 3. Intenta añadir el número 5 al set {1, 2, 3, 4, 5} nuevamente. ¿Qué sucede?
# No se sucede nada,se imprimirá el set tal y como esta. Esto debido a que en los sets no pueden haber elementos repetidos.

# 4. Verifica si el número 3 está en el set {1, 2, 3, 4, 5} e imprime el resultado.
print('Ejercicio #4')
print(3 in my_set,'\n')

# 5. Elimina el número 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.
print('Ejercicio #5')
my_set.remove(4)
print(f'{my_set}\n')

# 6. Usa el método clear() para vaciar un set y luego imprime su longitud.
print('Ejercicio #6')
my_set.clear()
print(len(my_set),'\n')

# 7. Convierte el set {"manzana", "naranja", "plátano"} en una lista e imprime el primer elemento de la lista.
print('Ejercicio #7')
my_set = {"manzana", "naranja", "plátano"}
my_list = list(my_set)
print('El 1er elemento de la lista es:',my_list[0],'\n')

# 8. Realiza la unión de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.
print('Ejercicio #8')
primer_set = {1, 2, 3}
segundo_set = {4, 5, 6}
nuevo_set = primer_set.union(segundo_set)
print(nuevo_set,'\n')

# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.
print('Ejercicio #9')
nuevo_set = {1, 2, 3, 4}.difference({3, 4, 5, 6})
print(nuevo_set,'\n')

# 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.
print('Ejercicio #10')
del my_set
print(my_set) #name 'my_set' is not defined