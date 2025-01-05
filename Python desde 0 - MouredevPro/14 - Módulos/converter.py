# Crea un módulo llamado "converter" que tenga funciones para convertir temperaturas entre Celsius y Fahrenheit. Escribe un programa que importe este módulo y realice conversiones.
def celsius_to_fahrenheit(temperatura):
    fahrenheit = ((temperatura * (9/5)) + 32)
    fahrenheit_redondeado = round(fahrenheit, 2)
    print(f'{temperatura}°C a Fahrenheit son: {fahrenheit_redondeado}°F')

def fahrenheit_to_celsius(temperatura):
    celsius = (temperatura - 32) * (5/9)
    celsius_redondeado = round(celsius, 2)
    print(f'{temperatura}°F a Celsius son: {celsius_redondeado}°C')