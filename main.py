import modulo_funciones.funciones as func

# Programa principal
def main():
    productos = []

    while True:
        func.limpiar_pantalla()
        func.mostrar_menu()
        opcion = input(func.estilo_input + "Seleccione una opción: ")

        if not func.es_entero(opcion):
            print(func.estilo_input + "Ingrese una entrada válida.")
            func.esperar()
            continue

        opcion = int(opcion)
        if opcion not in range(1, 6):
            print(func.estilo_alerta + "Número incorrecto.")
            func.esperar()
            continue

        if opcion == 1:
            productos = func.agregar_producto(productos)
            
        elif opcion == 2:
            func.mostrar_productos(productos)
        elif opcion == 3:
            resultados = func.buscar_producto(productos)
            if resultados:
                for p in resultados:
                    print(func.estilo_informe + f"Encontrado: {p[0]} - {p[1]} - ${p[2]} - {p[3]}")
            else:
                print(func.estilo_alerta + "No se encontraron resultados.")
            func.esperar()
        elif opcion == 4:
            productos = func.eliminar_producto(productos)
        elif opcion == 5:
            func.limpiar_pantalla()
            print(func.estilo_menu_bg + "Gracias por usar el sistema.")
            break

if __name__ == "__main__":
    main()
