## Strings
**¿Qué son los strings?**
Son secuencias de caracteres utilizadas para representar texto. Cualquier cosa que este escrita en "" o '' se le considerada un string.
```python
my_string = "Mi String"
my_other_string = 'Mi otro String'
```

**Inmutabilidad**
Los strings en Python son **inmutables**, lo que significa que no se pueden modificar una vez creados. Si necesitas cambiar un string, debes crear uno nuevo.
```python
texto = "Hola" # texto[0] = "h" # Esto dará un error 
texto = "hola" # Esto crea un nuevo string
```

**Salto de línea**
```python
my_new_line_string = "Este es un String\ncon salto de línea"
```

**Tabulación**
```python
my_tab_string = "\tEste es un String con tabulación"
```

**Operaciones básicas**
```python
saludo = "Hola" + " Mundo" 
print(saludo) # "Hola Mundo"

eco = "Echo " * 3
print(eco)  # "Echo Echo Echo "

print(len("Hola"))  # 4
```

**Índices y Slicing**
```python
palabra = "Python"
print(palabra[0])  # "P"
print(palabra[-1])  # "n" (índice negativo para contar desde el final)

#Extraer subcadenas con slicing
palabra = "Python"
print(palabra[0:3])  # "Pyt" (del índice 0 al 2)
print(palabra[:3])   # "Pyt" (desde el inicio hasta el 2)
print(palabra[3:])   # "hon" (desde el índice 3 hasta el final)
```

**Métodos Comunes**
```python
#Mayúsculas y minúsculas
texto = "hola"
print(texto.upper())  # "HOLA"
print(texto.lower())  # "hola"
print(texto.capitalize())  # "Hola"

#Buscar y reemplazar
texto = "Hola Mundo"
print(texto.find("Mundo"))  # 5 (posición)
print(texto.replace("Mundo", "Python"))  # "Hola Python"

#Eliminar espacios
texto = "  Hola  "
print(texto.strip())  # "Hola" (quita espacios al inicio y al final)

#Separar y unir
texto = "Hola Mundo Python"
palabras = texto.split()  # ['Hola', 'Mundo', 'Python']
print(" ".join(palabras))  # "Hola Mundo Python"
```

**Formatos de String**
```python
#Interpolación(f-strings)
nombre = "Alejandro"
edad = 23
print(f"Me llamo {nombre} y tengo {edad} años.")

#Método format()
print("Me llamo {} y tengo {} años.".format("Alejandro", 23))
```