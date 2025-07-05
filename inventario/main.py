import os
import mod_frontend as front
import mod_backend as back

def main(database):
    while True:
        front.limpiar_pantalla()
        front.mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion not in range(1, 8):
                raise ValueError("Opción fuera de rango")
        except ValueError:
            print("Entrada inválida. Ingrese un número del 12 al 7.")
            front.esperar()
            continue

        if opcion == 1:
            front.agregar_producto(database)
        elif opcion == 2:
            front.mostrar_productos(database)
        elif opcion == 3:
            front.buscar_producto(database)
        elif opcion == 4:
            front.actualizar_producto(database)
        elif opcion == 5:
            front.eliminar_producto(database)
        elif opcion == 6:
            front.reporte_stock(database)
        elif opcion == 7:
            front.limpiar_pantalla()
            print("Gracias por usar el sistema.")
            break

def crear_base_datos():
    carpeta_base = os.path.dirname(os.path.abspath(__file__)) 
    database = os.path.join(carpeta_base, "data", "data.db")
    # Crear base y tabla (si no existe) antes de iniciar la app
    back.crear_base_datos(database)
    back.crear_tabla_productos(database)
    return database



if __name__ == "__main__":
    database = crear_base_datos()
    main(database)
    

