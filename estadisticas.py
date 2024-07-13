import math
import globales

def generar_promedio_personas():
    todos_los_destino = globales.leer_archivo_json('destinos.json')
    cant_pers_reserva = 0
    
    for destinos in todos_los_destino:
        cant_pers_reserva += destinos['cant_personas']
    promedio = cant_pers_reserva / len(todos_los_destino)
    print(f"El promedio de las personas por reserva es:",promedio)

def media_geometrica():
    todos_los_destino = globales.leer_archivo_json('destinos.json')
    cant_pers_reserva = 0
    
    for destinos in todos_los_destino:
        cant_pers_reserva += math.log(destinos['costo'])
    promedio = math.exp(cant_pers_reserva / len(todos_los_destino))
    print(f"La media geometrica es:",promedio)




    
        