import os
import globales
import destinos
import estadisticas
os.system("cls")

def menu_principal():
    while True:
        os.system("cls")
        print("1. Asignar costos aleatorios a los destinos")
        print("2. Clasificar destinos por costo")
        print("3. Ver estadísticas de reservas")
        print("4. Reporte de reservas")
        print("5. Salir del programa")
        opcion = globales.seleccionar_opcion(5)
        
        if opcion == 1:
            print("1. Asignar costos aleatorios a los destinos")
            destinos.asignar_costos_aleatorios()
        elif opcion == 2:
            print("2. Clasificar destinos por costo")
        elif opcion == 3:
            print("3. Ver estadísticas de reservas")
            menu_estadisticas()
        elif opcion == 4:
            print("4. Reporte de reservas")
            destinos.reporte_csv()
        elif opcion == 5:
            print("5. Salir del programa")
            print("Desarrollado por Luis Sandoval")
            return
        input()

def menu_estadisticas():
    while True:
        os.system("cls")
        print("1. Total de reservas")
        print("2. Destino más reservado")
        print("3. Promedio de personas por reserva")
        print("4. Media Geométrica del valor de reserva")
        print("5. Volver")
        opcion = globales.seleccionar_opcion(5)
        
        if opcion == 1:
            print("1. Total de reservas")
        elif opcion == 2:
            print("2. Destino más reservado")
        elif opcion == 3:
            print("3. Promedio de personas por reserva")
            estadisticas.generar_promedio_personas()
        elif opcion == 4:
            print("4. Media Geométrica del valor de reserva")
            estadisticas.media_geometrica()
        elif opcion == 5:
            print("5. Volver")
            return
        input()

menu_principal()
        
