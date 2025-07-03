import os
import mod_backend as bd


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausa():
    os.system('pause' if os.name == 'nt' else 'read -e -n 1 -p \
               "Presione una tecla para continuar..."')
    return None 

    #input("Presione Enter para continuar.")


def mostrar_menu():
    print("\n")
    print( "**************************************")
    print( "Sistema de Gestión Básica De Productos")
    print( "**************************************\n")
    print(
        "1. Agregar producto\n"
        "2. Mostrar productos\n"
        "3. Buscar producto por id\n"
        "4. Actualizar producto por id\n"
        "5. Eliminar producto por id\n"
        "6. Reportes de Stock\n"
        "7. Salir" 
    )



def agregar_producto(database): # ingreso de datos mediante la consola
    try:
        nombre = input("Ingrese nombre de producto: ").capitalize().strip()
        descripcion = input("Ingrese la descripción: ").capitalize().strip()
        cantidad_input = input("Ingrese cantidad: ").strip()
        precio_input = float(input( "Ingrese el precio: ").strip())
        categoria = input("Ingrese categoría: ").capitalize().strip()

        # Validaciones
        if not nombre or not categoria:
            raise ValueError("No se permiten valores vacíos.")

        cantidad = int(cantidad_input)
        precio = float(precio_input)

        # Insertar en base de datos usando función del modulo base_datos (bd)
        bd.insertar_producto(database, nombre, descripcion, cantidad, precio, categoria)
        print("Producto agregado correctamente.")

    except ValueError as e:
        print(str(e))
    except Exception as e:
        print( f"Ocurrió un error inesperado: {e}")
    pausa()



def mostrar_productos(database):
    """
    Solicita a la base_datos los productos y los muestra por consola.
    """
    productos = bd.obtener_productos(database)

    if productos:
        print("\nListado de productos:")
        for p in productos:
            print(f"ID: {p[0]:<3} | Nombre: {p[1]:<15} | Descripción: {p[2]:<20} | "
                  f"Cantidad: {p[3]:<8} | Precio: ${p[4]:<8.2f} | Categoría: {p[5]:<10} | "
                  f"Modificado: {p[6]:<19}")
    else:
        print("No hay productos registrados en la base de datos.")

    pausa()


def buscar_producto(database):
    try:
        id_input = input("Ingrese el ID del producto a buscar: ").strip()
        if not id_input.isdigit():
            raise ValueError("El ID debe ser un número entero.")

        producto_id = int(id_input)
        resultado = bd.buscar_producto_por_id(database, producto_id)

        if resultado:
            print(f"\nProducto encontrado:")
            print(f"ID: {resultado[0]:<3} | Nombre: {resultado[1]:<15} | Descripción: {resultado[2]:20} | "
                  f"Cantidad: {resultado[3]:<8} | Precio: ${resultado[4]:<8.2f} | Categoría: {resultado[5]:<10} | "
                  f"Modificado: {resultado[6]:<19}")
        else:
            print("No se encontró ningún producto con ese ID.")

    except ValueError as e:
        print(str(e))
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

    pausa()


def actualizar_producto(database):
    try:
        producto_id_input = input("Ingrese el ID del producto a actualizar: ").strip()
        if not producto_id_input.isdigit():
            raise ValueError("El ID debe ser un número entero.")
        producto_id = int(producto_id_input)

        producto = bd.buscar_producto_por_id(database, producto_id) #reutiliza codigo
        if not producto:
            print("No se encontró un producto con ese ID.")
            pausa()
            return

        print(f"\nProducto actual:")
        print(f"ID: {producto[0]:<3} | Nombre: {producto[1]:<15} | Descripción: {producto[2]:<20} | "
              f"Cantidad: {producto[3]:<8} | Precio: ${producto[4]:<8.2f} | Categoría: {producto[5]:<10} | "
              f"Modificado: {producto[6]:<19}")

        print("\nIngrese los nuevos valores o vacío para mantener el actual):")

        nombre = input(f"Nuevo nombre [{producto[1]}]: ").strip().capitalize() or producto[1] # si dejamos vacio el campo "or" mantiene el valor anterior
        descripcion = input(f"Nueva descripción [{producto[2]}]: ").strip() or producto[2]
        cantidad_input = input(f"Nueva cantidad [{producto[3]}]: ").strip()
        precio_input = input(f"Nuevo precio [{producto[4]}]: ").strip()
        categoria = input(f"Nueva categoría [{producto[5]}]: ").strip().capitalize() or producto[5]

        cantidad = int(cantidad_input) if cantidad_input else producto[3]
        precio = float(precio_input) if precio_input else producto[4]

        actualizado = bd.actualizar_producto_por_id(database, producto_id, nombre, descripcion, cantidad, precio, categoria)

        if actualizado:
            print("Producto actualizado correctamente.")
        else:
            print("No se pudo actualizar el producto.")

    except ValueError as e:
        print(str(e))
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    pausa()


def eliminar_producto(database):
    try:
        id_input = input("Ingrese el ID del producto a eliminar: ").strip()
        if not id_input.isdigit():
            raise ValueError("El ID debe ser un número entero.")

        producto_id = int(id_input)

        # Obtener el producto antes de eliminarlo
        producto = bd.buscar_producto_por_id(database, producto_id) # reutiliza funcion 
        if not producto:
            print("No se encontró un producto con ese ID.")
            pausa()
            return

        print(f"\nProducto a eliminar:")
        print(f"ID: {producto[0]:<3} | Nombre: {producto[1]:<15} | Descripción: {producto[2]:<20} | "
              f"Cantidad: {producto[3]:<8} | Precio: ${producto[4]:<8.2f} | Categoría: {producto[5]:<10} | "
              f"Modificado: {producto[6]:<19}")

        confirmar = input("¿Está seguro que desea eliminar este producto? (s/n): ").lower()
        if confirmar == 's':
            eliminado = bd.eliminar_producto_por_id(database, producto_id)
            if eliminado:
                print("Producto eliminado correctamente.")
            else:
                print("No se pudo eliminar el producto.")
        else:
            print("Eliminación cancelada.")

    except ValueError as e:
        print(str(e))
    except Exception as e:
        print(f"Error inesperado: {e}")
    pausa()


def reporte_stock(database):
    try:
        limite_input = input("Ingrese el límite de stock (cantidad máxima): ").strip()
        if not limite_input.isdigit():
            raise ValueError("El límite debe ser un número entero.")

        limite = int(limite_input)
        productos = bd.obtener_productos_con_stock_bajo(database, limite)

        if not productos:
            print(f"No hay productos con stock igual o inferior a {limite}.")
        else:
            print(f"\nProductos con stock ≤ {limite}:\n")
            for p in productos:
                print(f"ID: {p[0]:<3} | Nombre: {p[1]:<15} Descripción: {p[2]:<20} | "
                      f"Cantidad: {p[3]:<8} | Precio: ${p[4]:<8.2f} | Categoría: {p[5]:<10} | "
                      f"Modificado: {p[6]:<19}")

    except ValueError as e:
        print(str(e))
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    pausa()

def main():
    print("Este script se está ejecutando directamente.")

if __name__ == '__main__':
    main() 
    