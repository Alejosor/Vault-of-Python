## Tuples
**¿Qué son las tuplas?**
Las tuplas son estructuras de datos ordenadas e inmutables en Python que permiten almacenar múltiples valores, los cuales pueden ser de diferentes tipos. Se definen con `()` o con la función `tuple()`.

```python

my_tuple = tuple()

my_other_tuple = ()

  

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

my_other_tuple = (35, 60, 30)

  

print(my_tuple) # (35, 1.77, "Brais", "Moure", "Brais")

print(type(my_tuple)) # <class 'tuple'>

```


**Acceso a elementos y búsqueda**
Se puede acceder a los elementos de una tupla utilizando índices (positivos o negativos).
Las tuplas, al ser inmutables, no permiten la modificación directa de sus elementos.

```python

print(my_tuple[0]) # 35

print(my_tuple[-1]) # "Brais"

# print(my_tuple[4]) # IndexError

# print(my_tuple[-6]) # IndexError

```

- **Contar elementos repetidos:**
```python

print(my_tuple.count("Brais")) # 2

```
  
- **Buscar índice de un elemento:**
```python

print(my_tuple.index("Moure")) # 3

print(my_tuple.index("Brais")) # 0 (primer índice encontrado)

```


**Concatenación de tuplas**
Se pueden unir dos tuplas utilizando `+`.
```python

my_sum_tuple = my_tuple + my_other_tuple

print(my_sum_tuple)

# (35, 1.77, "Brais", "Moure", "Brais", 35, 60, 30)

```

**Subtuplas**
Puedes obtener una parte de la tupla utilizando **slicing**.
```python

print(my_sum_tuple[3:6])

# ("Moure", "Brais", 35)

```

**Tupla mutable con conversión a lista**
Aunque las tuplas son inmutables, puedes convertirlas en listas para modificarlas y luego volver a convertirlas en tuplas.
```python

my_tuple = list(my_tuple)

print(type(my_tuple)) # <class 'list'>

  

my_tuple[4] = "MoureDev"

my_tuple.insert(1, "Azul")

my_tuple = tuple(my_tuple)

print(my_tuple)

# (35, "Azul", 1.77, "Brais", "Moure", "MoureDev")

print(type(my_tuple)) # <class 'tuple'>

```
  
**Eliminación de tuplas**
No se pueden eliminar elementos individuales de una tupla, pero puedes eliminar la tupla completa con `del`.
```python

del my_tuple

# print(my_tuple) # NameError: name 'my_tuple' is not defined

```