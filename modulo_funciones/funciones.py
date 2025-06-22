import os
import datetime
from colorama import init, Fore, Back, Style

init(autoreset=True) # reinicio a valroes por defecto despues de cada impresion

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

estilo_menu = Style.BRIGHT + Fore.GREEN
estilo_menu_bg = Style.BRIGHT + Fore.GREEN + Back.YELLOW
estilo_input = Style.BRIGHT + Fore.BLUE
estilo_alerta = Style.BRIGHT + Fore.RED
estilo_informe = Style.BRIGHT + Fore.YELLOW

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

def es_entero(valor):
    return valor.isdigit() #devuelve True si el valor es digito entero


def agregar_producto(productos):
    try:
        nombre = input(estilo_input + "Ingrese nombre de producto: ").capitalize().strip()
        categoria = input(estilo_input + "Ingrese categoría: ").capitalize().strip()
        precio_input = input(estilo_input + "Ingrese el precio (sin centavos): ").strip()
        fecha_y_hora_compra = datetime.datetime.now().strftime("%d-%m-%y %H:%M")

        if not nombre or not categoria:
            raise ValueError("No se permiten valores vacíos.")

        if not es_entero(precio_input):
            raise ValueError("El precio debe ser un número entero.")

        precio = int(precio_input)
        productos.append([nombre, categoria, precio, fecha_y_hora_compra])
        print(estilo_informe + "Producto agregado correctamente.")

    except ValueError as e:
        print(estilo_alerta + str(e))

    except Exception as e:
        print(estilo_alerta + f"Ocurrió un error inesperado: {e}")

    esperar()
    return productos


def mostrar_productos(productos):
    """
    Función para mostrar productos recibe como parametro las lista de productos.
    """
    if not productos:
        print(estilo_alerta + "No hay productos registrados.")
    else:
        print("\nListado de productos:")
        for producto in productos:
            print(estilo_informe + f" Producto: {producto[0]}\n - categoria: {producto[1]}\n - Precio: ${producto[2]}\n - fecha y hora de compra: {producto[3]}\n")
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
