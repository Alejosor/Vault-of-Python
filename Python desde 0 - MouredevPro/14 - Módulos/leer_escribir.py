# 7. Escribe un módulo que contenga funciones para leer y escribir en archivos de texto. Crea un programa que use estas funciones para escribir y leer datos.
def leer(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def escribir(nombre_archivo, contenido):
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(contenido)
            print(f"Datos escritos en el archivo '{nombre_archivo}' con éxito.")
    except Exception as e:
        print(f"Error inesperado: {e}")