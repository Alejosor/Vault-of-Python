### Operadores Aritméticos ###

# Operaciones con enteros
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)
print(2 ** 3)
print(2 ** 3 + 3 - 7 / 1 // 4)

# Operaciones con cadenas de texto
print("Hola " + "Python " + "¿Qué tal?")
print("Hola " + str(5))

# Operaciones mixtas
print("Hola " * 5)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operadores de asignación ###

# Asignación simple
x = 5
print("Asignación (x = 5):", x)  # 5

# Suma y asigna
x += 3  # x = x + 3
print("Suma y asigna (x += 3):", x)  # 8

# Resta y asigna
x -= 2  # x = x - 2
print("Resta y asigna (x -= 2):", x)  # 6

# Multiplica y asigna
x *= 4  # x = x * 4
print("Multiplica y asigna (x *= 4):", x)  # 24

# Divide y asigna
x /= 2  # x = x / 2
print("Divide y asigna (x /= 2):", x)  # 12.0

# División entera y asigna
x //= 2  # x = x // 2
print("División entera y asigna (x //= 2):", x)  # 6.0

# Módulo y asigna
x %= 3  # x = x % 3
print("Módulo y asigna (x %= 3):", x)  # 0.0

# Exponenciación y asigna
x = 2
x **= 3  # x = x ** 3
print("Exponenciación y asigna (x **= 3):", x)  # 8


### Operadores Comparativos ###

# Operaciones con enteros
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

# Operaciones con cadenas de texto
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

### Operadores Lógicos ###

# Basada en el Álgebra de Boole
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))