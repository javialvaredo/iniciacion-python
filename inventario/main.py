import os
import funciones as func




def main(database):
    while True:
        func.limpiar_pantalla()
        func.mostrar_menu()

        try:
            opcion = int(input(func.estilo_input + "Seleccione una opción: "))
            if opcion not in range(1, 6):
                raise ValueError("Opción fuera de rango")
        except ValueError:
            print(func.estilo_alerta + "Entrada inválida. Ingrese un número del 1 al 5.")
            func.esperar()
            continue

        if opcion == 1:
            productos = func.agregar_producto(database)
        elif opcion == 2:
            func.mostrar_productos(database)
        elif opcion == 3:
            resultados = func.buscar_producto(database)
            if resultados:
                for p in resultados:
                    print(func.estilo_informe + f"Encontrado: {p[0]} - {p[1]} - ${p[2]} - {p[3]}")
            else:
                print(func.estilo_alerta + "No se encontraron resultados.")
            func.esperar()
        elif opcion == 4:
            productos = func.eliminar_producto(database)
        elif opcion == 5:
            func.limpiar_pantalla()
            print(func.estilo_menu_bg + "Gracias por usar el sistema.")
            break

if __name__ == "__main__":
    carpeta_base = os.path.dirname(os.path.abspath(__file__)) #usar rutas absolutas dinamicas par ekecutar de cualuier carpeta
    database = os.path.join(carpeta_base, "data", "inventario.db")
    main(database)
    

