# 5. Escribe un módulo que contenga una función que acepte cualquier número de argumentos y devuelva su suma. Importa y usa la función en otro archivo.
def suma_argumentos(*numeros):
    print(sum(numeros))