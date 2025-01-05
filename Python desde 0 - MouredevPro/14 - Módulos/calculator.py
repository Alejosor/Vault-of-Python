def sumar(num1,num2):
    return num1 + num2

def restar(num1,num2):
    return num1-num2

def multiplicar(num1,num2):
    return num1*num2

def dividir(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError as e:
        print(f'Error: Recordar que no se puede dividir un número por 0,\ne\{e}')
    except Exception as exception:
        print(f'Error detectado: {exception}')
    finally:
        print('Programa terminado.')