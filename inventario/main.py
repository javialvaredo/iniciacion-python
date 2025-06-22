import os
import funciones as func


def main(database):
    while True:
        func.limpiar_pantalla()
        func.mostrar_menu()

        try:
            opcion = int(input(func.estilo_input + "Seleccione una opción: "))
            if opcion not in range(1, 8):
                raise ValueError("Opción fuera de rango")
        except ValueError:
            print(func.estilo_alerta + "Entrada inválida. Ingrese un número del 1 al 7.")
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
            print(func.estilo_menu_bg + "Gracias por usar el sistema.")
            break

if __name__ == "__main__":
    carpeta_base = os.path.dirname(os.path.abspath(__file__)) #usar rutas absolutas dinamicas par ekecutar de cualuier carpeta
    database = os.path.join(carpeta_base, "data", "inventario.db")
    main(database) # enviamos la base de datos como parametro
    

