import os
from colorama import init, Fore, Back, Style
import base_datos as bd


# Estilos de salida de consola con colorama
estilo_menu = Style.BRIGHT + Fore.GREEN
estilo_menu_bg = Style.BRIGHT + Fore.GREEN + Back.YELLOW
estilo_input = Style.BRIGHT + Fore.BLUE
estilo_alerta = Style.BRIGHT + Fore.RED
estilo_informe = Style.BRIGHT + Fore.YELLOW


init(autoreset=True) # reinicio a valroes por defecto despues de cada impresion

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_menu():
    print("\n")
    print(estilo_menu_bg + "**************************************")
    print(estilo_menu_bg + "Sistema de Gestión Básica De Productos")
    print(estilo_menu_bg + "**************************************\n")
    print(
        estilo_menu +
        "1. Agregar producto\n"
        "2. Mostrar productos\n"
        "3. Buscar producto por id\n"
        "4. Actualizar producto por id\n"
        "5. Eliminar producto por id\n"
        "6. Reportes de Stock\n"
        "7. Salir" 
    )

def esperar():
    input(Fore.YELLOW + "Presione Enter para continuar.")


def agregar_producto(database): # ingreso de datos mediante la consola
    try:
        nombre = input(estilo_input + "Ingrese nombre de producto: ").capitalize().strip()
        descripcion = input(estilo_input + "Ingrese la descripción: ").capitalize().strip()
        cantidad_input = input(estilo_input + "Ingrese cantidad: ").strip()
        precio_input = float(input(estilo_input + "Ingrese el precio: ").strip())
        categoria = input(estilo_input + "Ingrese categoría: ").capitalize().strip()

        # Validaciones
        if not nombre or not categoria:
            raise ValueError("No se permiten valores vacíos.")

        cantidad = int(cantidad_input)
        precio = float(precio_input)

        # Insertar en base de datos usando función del modulo base_datos (bd)
        bd.insertar_producto(database, nombre, descripcion, cantidad, precio, categoria)
        print(estilo_informe + "Producto agregado correctamente.")

    except ValueError as e:
        print(estilo_alerta + str(e))
    except Exception as e:
        print(estilo_alerta + f"Ocurrió un error inesperado: {e}")
    esperar()



def mostrar_productos(database):
    """
    Solicita a la base_datos los productos y los muestra por consola.
    """
    productos = bd.obtener_productos(database)

    if productos:
        print("\nListado de productos:")
        for p in productos:
            print(estilo_informe +
                  f"ID: {p[0]} | Nombre: {p[1]} | Descripción: {p[2]} | "
                  f"Cantidad: {p[3]} | Precio: ${p[4]:.2f} | Categoría: {p[5]}"
                  f"Creado: {p[6]} | Modificado: {p[7]}")
    else:
        print(estilo_alerta + "No hay productos registrados en la base de datos.")

    esperar()


def buscar_producto(database):
    try:
        id_input = input(estilo_input + "Ingrese el ID del producto a buscar: ").strip()
        if not id_input.isdigit():
            raise ValueError("El ID debe ser un número entero.")

        producto_id = int(id_input)
        resultado = bd.buscar_producto_por_id(database, producto_id)

        if resultado:
            print(estilo_informe + f"\nProducto encontrado:")
            print(estilo_informe +
                  f"ID: {resultado[0]} | Nombre: {resultado[1]} | Descripción: {resultado[2]} | "
                  f"Cantidad: {resultado[3]} | Precio: ${resultado[4]:.2f} | Categoría: {resultado[5]}"
                  f"Creado: {resultado[6]} | Modificado: {resultado[7]}")
        else:
            print(estilo_alerta + "No se encontró ningún producto con ese ID.")

    except ValueError as e:
        print(estilo_alerta + str(e))
    except Exception as e:
        print(estilo_alerta + f"Ocurrió un error inesperado: {e}")

    esperar()


def actualizar_producto(database):
    try:
        producto_id_input = input(estilo_input + "Ingrese el ID del producto a actualizar: ").strip()
        if not producto_id_input.isdigit():
            raise ValueError("El ID debe ser un número entero.")
        producto_id = int(producto_id_input)

        producto = bd.buscar_producto_por_id(database, producto_id) #reutiliza codigo
        if not producto:
            print(estilo_alerta + "No se encontró un producto con ese ID.")
            esperar()
            return

        print(estilo_informe + f"\nProducto actual:")
        print(estilo_informe +
              f"ID: {producto[0]} | Nombre: {producto[1]} | Descripción: {producto[2]} | "
              f"Cantidad: {producto[3]} | Precio: ${producto[4]} | Categoría: {producto[5]}"
              f"Creado: {producto[6]} | Modificado: {producto[7]}")

        print(Fore.CYAN + "\nIngrese los nuevos valores o vacío para mantener el actual):")

        nombre = input(estilo_input + f"Nuevo nombre [{producto[1]}]: ").strip().capitalize() or producto[1] # si dejamos vacio el campo "or" mantiene el valor anterior
        descripcion = input(estilo_input + f"Nueva descripción [{producto[2]}]: ").strip() or producto[2]
        cantidad_input = input(estilo_input + f"Nueva cantidad [{producto[3]}]: ").strip()
        precio_input = input(estilo_input + f"Nuevo precio [{producto[4]}]: ").strip()
        categoria = input(estilo_input + f"Nueva categoría [{producto[5]}]: ").strip().capitalize() or producto[5]

        cantidad = int(cantidad_input) if cantidad_input else producto[3]
        precio = float(precio_input) if precio_input else producto[4]

        actualizado = bd.actualizar_producto_por_id(database, producto_id, nombre, descripcion, cantidad, precio, categoria)

        if actualizado:
            print(estilo_informe + "Producto actualizado correctamente.")
        else:
            print(estilo_alerta + "No se pudo actualizar el producto.")

    except ValueError as e:
        print(estilo_alerta + str(e))
    except Exception as e:
        print(estilo_alerta + f"Ocurrió un error inesperado: {e}")
    esperar()


def eliminar_producto(database):
    try:
        id_input = input(estilo_input + "Ingrese el ID del producto a eliminar: ").strip()
        if not id_input.isdigit():
            raise ValueError("El ID debe ser un número entero.")

        producto_id = int(id_input)

        # Obtener el producto antes de eliminarlo
        producto = bd.buscar_producto_por_id(database, producto_id) # reutiliza funcion 
        if not producto:
            print(estilo_alerta + "No se encontró un producto con ese ID.")
            esperar()
            return

        print(estilo_informe + f"\nProducto a eliminar:")
        print(estilo_informe +
              f"ID: {producto[0]} | Nombre: {producto[1]} | Cantidad: {producto[3]} | "
              f"Precio: ${producto[4]:.2f} | Categoría: {producto[5]} | "
              f"Creado: {producto[6]} | Modificado: {producto[7]}")

        confirmar = input(Fore.CYAN + "¿Está seguro que desea eliminar este producto? (s/n): ").lower()
        if confirmar == 's':
            eliminado = bd.eliminar_producto_por_id(database, producto_id)
            if eliminado:
                print(estilo_informe + "Producto eliminado correctamente.")
            else:
                print(estilo_alerta + "No se pudo eliminar el producto.")
        else:
            print(Fore.BLUE + "Eliminación cancelada.")

    except ValueError as e:
        print(estilo_alerta + str(e))
    except Exception as e:
        print(estilo_alerta + f"Error inesperado: {e}")
    esperar()


def reporte_stock(database):
    try:
        limite_input = input(estilo_input + "Ingrese el límite de stock (cantidad máxima): ").strip()
        if not limite_input.isdigit():
            raise ValueError("El límite debe ser un número entero.")

        limite = int(limite_input)
        productos = bd.obtener_productos_con_stock_bajo(database, limite)

        if not productos:
            print(estilo_alerta + f"No hay productos con stock igual o inferior a {limite}.")
        else:
            print(estilo_informe + f"\nProductos con stock ≤ {limite}:\n")
            for p in productos:
                print(estilo_informe +
                      f"ID: {p[0]} | Nombre: {p[1]} | Cantidad: {p[3]} | Precio: ${p[4]:.2f} | "
                      f"Categoría: {p[5]} | Creado: {p[6]} | Modificado: {p[7]}")

    except ValueError as e:
        print(estilo_alerta + str(e))
    except Exception as e:
        print(estilo_alerta + f"Ocurrió un error inesperado: {e}")
    esperar()



if __name__ == '__main__':
    pass #Evita que se ejecute el codigo automaticamente al ser importado desde otro archivo
    