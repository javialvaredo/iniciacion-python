import os
import datetime
from colorama import init, Fore, Back, Style
import base_datos as bd


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
        "3. Buscar producto\n"
        "4. Eliminar producto\n"
        "5. Salir" 
    )

def esperar():
    input(Fore.YELLOW + "Presione Enter para continuar.")


def agregar_producto(database):
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

        # Insertar en base de datos usando función de bd
        bd.insertar_producto(database, nombre, descripcion, cantidad, precio, categoria)
        print(estilo_informe + "Producto agregado a la base de datos correctamente.")

    except ValueError as e:
        print(estilo_alerta + str(e))
    except Exception as e:
        print(estilo_alerta + f"Ocurrió un error inesperado: {e}")
    esperar()



def mostrar_productos(database):
    import os
    print("Ruta absoluta a base de datos:", os.path.abspath(database))

    """
    Solicita a base_datos los productos y los muestra por consola.
    """
    productos = bd.obtener_productos(database)

    if productos:
        print("\nListado de productos:")
        for p in productos:
            print(estilo_informe + f"ID: {p[0]} | Nombre: {p[1]} | Descripción: {p[2]} | Cantidad: {p[3]} | Precio: ${p[4]:.2f} | Categoría: {p[5]}")
    else:
        print(estilo_alerta + "No hay productos registrados en la base de datos.")

    esperar()



    


def buscar_producto(productos):
    """
    Función para buscar un producto. Recibe como parametro las lista de productos.
    Devuelve una nueva lista con el producto buscado.
    """
    buscar = input(estilo_input + "Ingrese el nombre del producto a buscar: ").capitalize()
    resultados = []
    for p in productos:
        if p[0] == buscar:
            resultados.append(p)

    return resultados

def eliminar_producto(productos):
    try:
        producto_eliminar = input(estilo_input + "Ingrese el nombre del producto a eliminar: ").capitalize()
        for i, producto in enumerate(productos):
            if producto_eliminar == producto[0]:
                print(estilo_informe + f"Se va a eliminar: {producto[0]} - {producto[1]} - ${producto[2]}")
                confirmacion = input("¿Está seguro que desea eliminar este producto? (S/N): ").strip().lower()
                if confirmacion == 's':
                    productos.pop(i)
                    print(Fore.BLUE + "Producto eliminado.")
                else:
                    print(Fore.BLUE + "Eliminación cancelada.")
                break
        else:
            raise ValueError("Producto no figura ingresado en la lista.")

    except ValueError as e:
        print(estilo_alerta + str(e))

    except Exception as e:
        print(estilo_alerta + f"Ocurrió un error inesperado: {e}")

    esperar()
    return productos
