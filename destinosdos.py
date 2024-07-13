import random
import globales

def asignar_costos_aleatorios():
    destinos = ["Paris", 
                "Londres", 
                "Nueva York", 
                "Tokio", 
                "Sidney", 
                "Roma", 
                "Berlin", 
                "Barcelona"]
    
    personas = ["Juan Perez",
                "Maria Garcia",
                "Carlos Lopez",
                "Ana Martinez",
                "Pedro Rodriguez"]
    
    todos_los_destinos = []
    for nombre_destino in destinos:
        nombre = nombre_destino
        cliente = random.choice(personas)
        cantidadp = random.randint(1,4)
        costo = random.randint(100,1000)
        costo_total = int(cantidadp*costo)
        
        nuevo_destino = {
            'destino': nombre,
            'cliente': cliente,
            'cant_personas': cantidadp,
            'costo': costo,
            'costo_total':costo_total
        }
        
        todos_los_destinos.append(nuevo_destino)
        globales.guardar_archivo_json('destinos.json', todos_los_destinos)

def reporte_csv():
    todos_los_destinos = globales.leer_archivo_json('destinos.json')
    print("Nombre del Cliente  Destino Turistico  Cantidad de Personas  Costo Total")
    print("------------------------------------------------------------------------")
    for destino in todos_los_destinos:
        print(f"{destino['cliente']}\t\t{destino['destino']}\t\t{destino['cant_personas']}\t\t\t{destino['costo_total']}")
    fieldname = ['destino','cliente','cant_personas','costo','costo_total']
    globales.guardar_archivo_csv('Reporte_reservas.csv',todos_los_destinos,fieldname)

        
        
        
        
        
        