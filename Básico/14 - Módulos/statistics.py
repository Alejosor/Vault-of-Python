# 8. Crea un módulo llamado "statistics" que tenga funciones para calcular la media y la mediana de una lista de números. Usa este módulo para calcular estos valores en una lista dada.
def calcular_media(lista):
    suma_terminos = sum(lista)
    numero_terminos = len(lista)
    media = suma_terminos / numero_terminos
    print(f'La media de los números en la lista es: {media}')
    
def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    numero_terminos = len(lista_ordenada)
    mitad = numero_terminos // 2

    if numero_terminos % 2 == 0:
        mediana = (lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2
    else:
        mediana = lista_ordenada[mitad]

    print(f'La mediana de los números en la lista es: {mediana}')