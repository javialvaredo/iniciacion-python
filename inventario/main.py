import os
import mod_frontend as func
import mod_backend as bd


def main(database):
    while True:
        func.limpiar_pantalla()
        func.mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion not in range(1, 8):
                raise ValueError("Opción fuera de rango")
        except ValueError:
            print("Entrada inválida. Ingrese un número del 1 al 7.")
            func.esperar()
            continue

        if opcion == 1:
            func.agregar_producto(database)
        elif opcion == 2:
            func.mostrar_productos(database)
        elif opcion == 3:
            func.buscar_producto(database)
        elif opcion == 4:
            func.actualizar_producto(database)
        elif opcion == 5:
            func.eliminar_producto(database)
        elif opcion == 6:
            func.reporte_stock(database)
        elif opcion == 7:
            func.limpiar_pantalla()
            print("Gracias por usar el sistema.")
            break

def crear_base_datos():
    carpeta_base = os.path.dirname(os.path.abspath(__file__)) 
    database = os.path.join(carpeta_base, "data", "data.db")
    # Crear base y tabla (si no existe) antes de iniciar la app
    bd.crear_base_datos(database)
    bd.crear_tabla_productos(database)
    return database



if __name__ == "__main__":
    database = crear_base_datos()
    main(database)
    

