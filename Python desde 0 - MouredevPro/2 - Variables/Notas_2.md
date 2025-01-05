## Variables 
 Una variable es un nombre que se utiliza para almacenar datos. Las variables actúan como "contenedores" que guardan información que puede ser revisada y manipulada a lo largo de un programa.
 ```python
 numero = 10
 decimal = 3.14
 letras = 'Holaa'
 Bool = True
```
 
 ### **Declaración e Inicialización de Variables**
 En Python, no necesitamos declarar explícitamente el tipo de una variable. Simplemente asignamos un valor, y Python infiere el tipo de dato.
 
**¿Por qué no necesitamos declarar el tipo de dato?**	
No necesitamos declarar explícitamente el tipo de una variable porque es un lenguaje de tipado dinámico. Esto significa que el intérprete de Python determina automáticamente el tipo de dato de una variable en el momento de la asignación

 ### **Reglas para los nombres de las variables**
 - Deben comenzar con una letra o un guion bajo (_).
 - No pueden comenzar con un número.
 - Pueden contener letras, números y guiones bajos.
 - No pueden ser palabras reservadas de Python, como def, class, if, etc.

 ### **Asignación Múltiple**
 Podemos asignar múltiples variables en una sola línea.
 ```python
 a, b, c = 1, 2, "tres"
```

 ### **Variables Dinámicas**
 Las variables en Python son dinámicas, es decir, podemos cambiar su tipo en cualquier momento.
 ```python
 a, b, c = 1, 2, "tres"
```

 ### **Alcance de las Variables**
 - **Variables locales:** Definidas dentro de una función y solo accesibles allí.
 - **Variables globales:** Definidas fuera de las funciones y accesibles en todo el programa.
 ```python
 y = 100  # Variable global  
 
 def mi_funcion():     
	 z = 50  # Variable local     
	 print(z)  
 
 print(y)  # Accede a la variable global`
```