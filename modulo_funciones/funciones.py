import os
import datetime

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("\n")
    print("**************************************")
    print("Sistema de Gestión Básica De Productos")
    print("**************************************\n")
    print(
        "1. Agregar producto\n"
        "2. Mostrar productos\n"
        "3. Buscar producto\n"
        "4. Eliminar producto\n"
        "5. Salir"
    )

def esperar():
    input("Presione Enter para continuar.")

def es_entero(valor):
    return valor.isdigit() #devuelve True si el valor es digito entero

def agregar_producto(productos):
    """
    Función para agregar productos. recibe comp parametro la lista de productos y devuelve la lista actualizada.
    """
    

    nombre = input("Ingrese nombre de producto: ").capitalize().strip()
    categoria = input("Ingrese categoría: ").capitalize().strip()
    precio_input = input("Ingrese el precio (sin centavos): ").strip()
    fecha_y_hora_compra = datetime.datetime.now().strftime("%d-%m-%y %H:%M")


    if not nombre or not categoria:
        print("No se permiten valores vacíos.")
        esperar()
        

    if not es_entero(precio_input):
        print("El precio debe ser un número.")
        esperar()
        

    precio = int(precio_input)
    productos.append([nombre, categoria, precio, fecha_y_hora_compra])
    print("Producto agregado correctamente.")
    esperar()
    return productos

def mostrar_productos(productos):
    """
    Función para mostrar productos recibe como parametro las lista de productos.
    """
    if not productos:
        print("No hay productos registrados.")
    else:
        print("\nListado de productos:")
        for producto in productos:
            print(f" Producto: {producto[0]}\n - categoria: {producto[1]}\n - Precio: ${producto[2]}\n - fecha y hora de compra: {producto[3]}\n")
    esperar()

def buscar_producto(productos):
    """
    Función para buscar un producto. Recibe como parametro las lista de productos.
    Devuelve una nueva lista con el producto buscado.
    """
    buscar = input("Ingrese el nombre del producto a buscar: ").capitalize()
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
    producto_eliminar = input("Ingrese el nombre del producto a eliminar: ").capitalize()
    for i in range(len(productos)):
        if producto_eliminar == productos[i][0]:
            print(f"Se va a eliminar: {productos[i][0]} - {productos[i][1]} - ${productos[i][2]}")
            confirmacion = input("¿Está seguro que desea eliminar este producto? (S/N): ").strip().lower()
            if confirmacion == 's':
                productos.pop(i)
                print("Producto eliminado.")
            else:
                print("Eliminación cancelada.")
            esperar()
            return productos 
    
    print("Producto no figura ingresado en la lista.")
    esperar()
    return productos