import os
import datetime
from colorama import init, Fore, Back, Style

init(autoreset=True) # reinicio a valroes por defecto despues de cada impresion

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

estilo_menu = Style.BRIGHT + Fore.GREEN
estilo_input = Style.BRIGHT + Fore.BLUE
estilo_alerta = Style.BRIGHT + Fore.RED
estilo_informe = Style.BRIGHT + Fore.YELLOW

def mostrar_menu():
    print("\n")
    print(estilo_menu + "**************************************")
    print(estilo_menu + "Sistema de Gestión Básica De Productos")
    print(estilo_menu + "**************************************\n")
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
    """
    Función para agregar productos. recibe comp parametro la lista de productos y devuelve la lista actualizada.
    """
    
    nombre = input(estilo_input + "Ingrese nombre de producto: ").capitalize().strip()
    categoria = input(estilo_input + "Ingrese categoría: ").capitalize().strip()
    precio_input = input(estilo_input + "Ingrese el precio (sin centavos): ").strip()
    fecha_y_hora_compra = datetime.datetime.now().strftime("%d-%m-%y %H:%M")


    if not nombre or not categoria:
        print(estilo_alerta + "No se permiten valores vacíos.")
        esperar()
        return productos 

    if not es_entero(precio_input):
        print(estilo_alerta + "El precio debe ser un número.")
        esperar()
        return productos
        

    precio = int(precio_input)
    productos.append([nombre, categoria, precio, fecha_y_hora_compra])
    print(estilo_informe + "Producto agregado correctamente.")
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
    """
    Función para eliminar un producto.
    Recibe como parametro la lista de pdoructos y devuelve la lista actualizada.
    """
    producto_eliminar = input(estilo_input + "Ingrese el nombre del producto a eliminar: ").capitalize()
    for i in range(len(productos)):
        if producto_eliminar == productos[i][0]:
            print(estilo_informe + f"Se va a eliminar: {productos[i][0]} - {productos[i][1]} - ${productos[i][2]}")
            confirmacion = input("¿Está seguro que desea eliminar este producto? (S/N): ").strip().lower()
            if confirmacion == 's':
                productos.pop(i)
                print(Fore.BLUE + "Producto eliminado." )
            else:
                print(Fore.BLUE + "Eliminación cancelada.")
            esperar()
            return productos 
    
    print(estilo_alerta + "Producto no figura ingresado en la lista.")
    esperar()
    return productos