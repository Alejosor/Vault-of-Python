# 9. Crea un módulo que contenga una función para contar cuántas veces aparece una palabra en un texto. Escribe un programa que importe el módulo y lo use para contar palabras en una cadena.
def contador_palabra(palabra,texto):
    cantidad = texto.count(palabra) 
    print(f'La cantidad de veces que la palabra "{palabra}" se repite son: {cantidad}')