def generador_nombre():
    print('Bienvenido al generador de nombres para bandas, por favor responda las siguientes preguntas... ')
    animal_favorito = input('¿Cuál es su animal favorito?\n')
    color_favorito = input('¿Cuál es su color favorito?\n')
    print(f'Gracias por responder.\nEl nombre de su banda es "{animal_favorito} {color_favorito}".\nFin del programa')

generador_nombre()