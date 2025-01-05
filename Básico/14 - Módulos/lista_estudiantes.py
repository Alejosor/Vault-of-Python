# Crea un módulo que contenga una lista de nombres de estudiantes y una función que imprima todos los nombres. Importa este módulo en otro archivo y usa la función para mostrar la lista.
def lista_estudiantes():
    estudiantes = ['Alejo','Luis','Carlos','Lucas','Gabriel','Ricardo','Jorge']
    contador = 0
    for n in estudiantes:
        contador += 1
        print(f'Alumno #{contador}: {n}')
