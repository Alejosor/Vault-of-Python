# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.
print("Ejercicio #1")
my_dict = {"name":"Alejo", 
           "age":24, 
           "country":"Peru"}
print(f'Los valores del dict son {my_dict}\n')

# 2. Accede al valor de la clave name en el diccionario.
print("Ejercicio #2")
print('El valor de la clave name es',my_dict["name"],'\n')

# 3. Añade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.
print("Ejercicio #3")
my_dict["Job"] = "Programador"
print(f'Los nuevos valores del dict son {my_dict}\n')

# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.
print("Ejercicio #4")
my_dict["age"] = 38
print(f'Los nuevos valores del dict son {my_dict}\n')

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.
print("Ejercicio #5")
del my_dict["country"]
print(f'Los nuevos valores del dict son {my_dict}\n')

# 6. Crea un diccionario donde las claves sean números del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).
print("Ejercicio #6")
cuadrados = {x: x**2 for x in range(1,6)}
print(cuadrados,'\n')

# 7. Verifica si la clave age está presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.
print("Ejercicio #7")
print("age" in my_dict,'\n')

# 8. Imprime solo las claves del diccionario.
print("Ejercicio #8")
print(my_dict.keys(),'\n')

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.
print("Ejercicio #9")
print(list(my_dict.keys()),'\n')

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".
print("Ejercicio #10")
new_list = ["name", "age", "job"]
new_dict = dict.fromkeys(new_list,'Desconocido')
print(new_dict)