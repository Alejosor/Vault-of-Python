## Strings
**¿Qué son las listas?**
Las listas son estructuras de datos ordenadas y mutables en Python que permiten almacenar múltiples valores, los cuales pueden ser de diferentes tipos. Se definen con `[]` o con la función `list()`.
```python

my_list = list()

my_other_list = []

print(len(my_list)) # 0 (longitud de una lista vacía)

  

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list) # [35, 24, 62, 52, 30, 30, 17]

print(len(my_list)) # 7

```
 
**Tipos mixtos en listas**
Las listas pueden contener elementos de diferentes tipos.
```python

my_other_list = [35, 1.77, "Brais", "Moure"]

print(type(my_list)) # <class 'list'>

print(type(my_other_list)) # <class 'list'>

```

**Acceso a elementos y búsqueda**
Se puede acceder a los elementos de una lista utilizando índices (positivos o negativos).
Los índices negativos permiten acceder a los elementos desde el final.
```python
print(my_other_list[0]) # 35

print(my_other_list[1]) # 1.77

print(my_other_list[-1]) # "Moure"

print(my_other_list[-4]) # 35

```

- **Contar elementos repetidos:**
```python

print(my_list.count(30)) # 2

```

- **Buscar índice de un elemento:**
```python

print(my_other_list.index("Brais")) # 2

```

- **Desempaquetar valores:**
```python
age, height, name, surname = my_other_list

print(name) # "Brais"

```

**Concatenación de listas**
Se pueden unir dos listas utilizando `+`.
```python

print(my_list + my_other_list)

# [35, 24, 62, 52, 30, 30, 17, 35, 1.77, 'Brais', 'Moure']

```

**Creación, inserción, actualización y eliminación**
- **Agregar elementos con `append()`:**
```python

my_other_list.append("MoureDev")

print(my_other_list)

# [35, 1.77, "Brais", "Moure", "MoureDev"]

```

- **Insertar elementos con `insert()`:**
```python

my_other_list.insert(1, "Rojo")

print(my_other_list)

# [35, "Rojo", 1.77, "Brais", "Moure", "MoureDev"]

```

- **Actualizar valores directamente por índice:**
```python

my_other_list[1] = "Azul"

print(my_other_list)

# [35, "Azul", 1.77, "Brais", "Moure", "MoureDev"]

```

- **Eliminar elementos con `remove()`:**
```python

my_other_list.remove("Azul")

print(my_other_list)

# [35, 1.77, "Brais", "Moure", "MoureDev"]

```

- **Eliminar por posición con `pop()`:**
```python

my_pop_element = my_list.pop(2)

print(my_pop_element) # 62

print(my_list) # [35, 24, 52, 30, 30, 17]

```

- **Eliminar por índice con `del`:**
```python

del my_list[2]

print(my_list) # [35, 24, 30, 30, 17]

```
 
**Operaciones con listas**
- **Copiar listas:**
```python

my_new_list = my_list.copy()

```

- **Limpiar todos los elementos con `clear()`:**
```python

my_list.clear()

print(my_list) # []

```

- **Revertir el orden con `reverse()`:**
```python

my_new_list.reverse()

print(my_new_list)

```

- **Ordenar elementos con `sort()`:**
```python

my_new_list.sort()

print(my_new_list)

```

**Sublistas**
Puedes obtener una parte de la lista utilizando **slicing**.
```python

print(my_new_list[1:3])

# Devuelve los elementos desde el índice 1 hasta el 2 (excluyendo el 3)

```  

**Cambio de tipo**
Una lista puede ser reasignada a otro tipo de dato, pero perderá todas sus propiedades como lista.
```python

my_list = "Hola Python"

print(my_list) # "Hola Python"

print(type(my_list)) # <class 'str'>

```