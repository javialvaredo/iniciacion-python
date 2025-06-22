import sqlite3
import os
import main

def crear_base_datos(database):
    """
    Crea una base de datos SQLite si no existe.
    """
    if not os.path.exists(database):
        try:
            conexion = sqlite3.connect(database)
            print(f"Base de datos '{database}' creada correctamente.")
        except sqlite3.Error as e:
            print(f"Error al crear la base de datos: {e}")
        finally:
            if conexion:
                conexion.close()
    else:
        print(f"La base de datos '{database}' ya existe.")

def crear_tabla_productos(database):
    """
    Crea la tabla 'productos' si no existe.
    """
    try:
        conexion = sqlite3.connect(database)
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL,
                categoria TEXT
            )
        """)
        conexion.commit()
        print("Tabla 'productos' creada exitosamente.")

    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")

    finally:
        if conexion:
            conexion.close()


def insertar_producto(database, nombre, descripcion, cantidad, precio, categoria):
    """
    Inserta un producto en la tabla 'productos'.
    """
    conexion = None
    try:
        if not nombre or cantidad is None or precio is None:
            print("Nombre, cantidad y precio son obligatorios.")
            return

        conexion = sqlite3.connect(database)
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre, descripcion, cantidad, precio, categoria))
        conexion.commit()
        print("Producto insertado correctamente.")

    except sqlite3.Error as e:
        print(f"Error al insertar el producto: {e}")
    finally:
        if conexion:
            conexion.close()



def obtener_productos(database):
    """
    Recupera todos los productos de la base de datos.
    Retorna una lista de tuplas.
    """
    conexion = None
    try:
        conexion = sqlite3.connect(database)
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        return productos

    except sqlite3.Error as e:
        print(f"Error al acceder a la base de datos: {e}")
        return []

    finally:
        if conexion:
            conexion.close()


   

if __name__ == '__main__':
    pass
    