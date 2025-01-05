# 10 Crea un módulo llamado "dates" que contenga funciones para obtener la fecha actual y calcular la diferencia entre dos fechas. Usa este módulo en un programa para mostrar la fecha actual y la diferencia entre dos fechas específicas.
import datetime

def obtener_fecha_actual():
    fecha_actual = datetime.datetime.now().date()
    fecha_actual_formateada = fecha_actual.strftime("%d/%m/%Y")
    print(f'La fecha actual es: {fecha_actual_formateada}')
    return fecha_actual

def diferencia_fechas(fecha1, fecha2):
    if isinstance(fecha1, str):
        fecha1 = datetime.datetime.strptime(fecha1, "%d/%m/%Y").date()
    if isinstance(fecha2, str):
        fecha2 = datetime.datetime.strptime(fecha2, "%d/%m/%Y").date()
    
    diferencia = abs((fecha2 - fecha1).days)
    print(f'La diferencia de días entre {fecha1.strftime("%d/%m/%Y")} y {fecha2.strftime("%d/%m/%Y")} es de: {diferencia} días')
    return diferencia