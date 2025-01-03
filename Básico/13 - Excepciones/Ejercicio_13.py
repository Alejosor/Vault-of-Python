# 1. Crea una función que intente dividir dos números proporcionados por el usuario. Usa try-except para capturar cualquier error de división (por ejemplo, división por cero).
def dividir_numeros():
    try:
        num1 = int(input('Ingrese un número:\n'))
        num2 = int(input('Ingrese otro número:\n'))
        division = num1 / num2
        print(f'El resultado de la división es: {division}')
    except ZeroDivisionError:
        print('Error: No se puede dividir por cero.')
    except ValueError:
        print('Error: Por favor, ingrese un número válido.')
    except Exception as e:
        print(f'Ocurrió un error: {e}')

# 2. Crea una función que tome una cadena e intente convertirla en un número entero. Usa try-except para capturar cualquier error en la conversión.
def cadena_invertida():
    try:
        cadena_a_numero = int(input('Ingrese su número:\n'))
        print(f'Este es su número: {cadena_a_numero}')
    except ValueError:
        print('Error: No se puede convertir la cadena a número.')

# 3. Crea una función que abra un archivo, lea su contenido y maneje posibles errores (por ejemplo, archivo no encontrado). Usa try-except para gestionar las operaciones de archivos de forma segura.
def abrir_archivo(archivo):
    try:
        with open(archivo,'r') as file:
            contenido = file.read()
            print('El archivo a sido abierto con éxito.')
            return contenido
    except FileNotFoundError as e:
        print('El archivo no ha podido ser encontrado')
        print(e)
    except Exception as exception:
        print('Error detectado')
        print(exception)

# 4. Crea una función que realice múltiples operaciones (suma, resta, división, multiplicación) con dos números. Usa try-except-else-finally para manejar errores y asegurar que se imprima un mensaje final, independientemente de los errores.


def multiples_operaciones():
    try:
        num1 = int(input('Ingrese su 1er número:'))
        num2 = int(input('Ingrese su 2do número:'))
        suma = num1 + num2
        resta = num1 - num2
        multi = num1 * num2
        divi = num1 / num2
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except ValueError:
        print("Se ha producido un ValueError")
    except TypeError:
        print("Se ha producido un TypeError")
    except Exception as e:    
        print('Se a detectado un error inesperado, por favor vuelva a intentar.')
        print(e)
    else:
        print('Resultados:')
        print(f'- Suma: {suma}')
        print(f'- Resta: {resta}')
        print(f'- Multiplicación: {multi}')
        print(f'- División: {divi}')
    finally:
        print('Programa ejecutado correctamente.')
    
# 5. Crea una función que le pida al usuario su edad y lance un ValueError si la entrada no es un número entero positivo. Usa el manejo de excepciones para gestionar la entrada y lanzar excepciones personalizadas cuando sea necesario.

# 6. Crea una función que intente acceder a un elemento de una lista por índice. Usa try-except para manejar el caso donde el índice esté fuera de rango.

# 7. Crea una función que use try-except para manejar múltiples excepciones: ZeroDivisionError, ValueError y TypeError.

# 8. Crea una función que simule una transacción. Lanza una excepción personalizada llamada InsufficientFundsError si el saldo es menor que la cantidad a retirar.

# 9. Crea una función que intente convertir una lista de cadenas en enteros. Maneja cualquier error que surja cuando una cadena no pueda convertirse.

# 10. Crea una función que calcule la raíz cuadrada de un número. Lanza un ValueError si el número es negativo.
