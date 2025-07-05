import sqlite3
import os
import sys


#------------ Crear base de dato y tabla si no existen --------------
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
            nombre TEXT NOT NULL CHECK(nombre <> ''),
            descripcion TEXT,
            cantidad INTEGER NOT NULL CHECK(cantidad >= 0),
            precio REAL NOT NULL CHECK(precio >= 0),
            categoria TEXT,
            actualizado_en TEXT
            );
        """)
        conexion.commit()
        print("Tabla 'productos' creada exitosamente.")

    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")
    except sqlite3.DatabaseError:
        print(f"Error de base de datos, revisar la integridad del archivo {database}")
        sys.exit()


    finally:
        if conexion:
            conexion.close()


# ------------Funciones CRUD en la base de datos ---------------
def insertar_producto(database, nombre, descripcion, cantidad, precio, categoria, actualizado_en):
    """
    Agrega un registro a la tabla 'productos'.
    """
    conexion = None
    try:
        if not nombre or cantidad is None or precio is None:
            print("Nombre, cantidad y precio son obligatorios.")
            return

        conexion = sqlite3.connect(database)
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria, actualizado_en)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nombre, descripcion, cantidad, precio, categoria, actualizado_en))
        conexion.commit()

    except sqlite3.IntegrityError as e:
        if conexion:
            conexion.rollback()
        print("Error: los datos no cumplen las restricciones de la base de datos.")

    except sqlite3.DatabaseError:
        if conexion:
            conexion.rollback()
        print(f"Error de base de datos, revisar la integridad del archivo {database}")
        sys.exit()

    except sqlite3.Error as e:
        if conexion:
            conexion.rollback()
        print(f"Error al insertar el producto: {e}")

    finally:
        if conexion:
            conexion.close()




def obtener_productos(database):
    """
    Ejecuta la consulta en la base de datos.
    """
    conexion = None
    productos = []
    try:
        conexion = sqlite3.connect(database)
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()

    except sqlite3.DatabaseError:
        print(f"Error de base de datos, revisar la integridad del archivo {database}")
        sys.exit()

    except sqlite3.Error as e:
        print(f"Error al acceder a la base de datos: {e}")

    finally:
        if conexion:
            conexion.close()

    return productos



def buscar_producto_por_id(database, producto_id):
    """
    Busca un producto por su id en la base de datos.
    """
    conexion = None
    try:
        conexion = sqlite3.connect(database)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = ?", (producto_id,))
        resultado = cursor.fetchone()
        return resultado  # Devuelve una tupla o None si no lo encuentra

    except sqlite3.DatabaseError:
        print(f"Error de base de datos, revisar la integridad del archivo {database}")
        sys.exit()

    except sqlite3.Error as e:
        print(f"Error al acceder a la base de datos: {e}")
        return None

    finally:
        if conexion:
            conexion.close()



def actualizar_producto_por_id(database, producto_id, nombre, descripcion, cantidad, precio, categoria, actualizado_en):
    """
    Actualiza un producto en la base de datos por su ID.
    """
    conexion = None
    try:
        conexion = sqlite3.connect(database)
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE productos
            SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?, actualizado_en = ?
            WHERE id = ?
        """, (nombre, descripcion, cantidad, precio, categoria, actualizado_en, producto_id))

        conexion.commit()

        return cursor.rowcount > 0  # True si actualizó algo

    except sqlite3.DatabaseError:
        if conexion:
            conexion.rollback()
        print(f"Error de base de datos, revisar la integridad del archivo {database}")
        sys.exit()

    except sqlite3.Error as e:
        if conexion:
            conexion.rollback()
        print(f"Error al actualizar el producto: {e}")
        return False

    finally:
        if conexion:
            conexion.close()



def eliminar_producto_por_id(database, producto_id):
    """
    Elimina un producto por su ID.
    Devuelve True si se eliminó, False si no se encontró.
    """
    conexion = None
    try:
        conexion = sqlite3.connect(database)
        cursor = conexion.cursor()

        # Verificamos que exista
        cursor.execute("SELECT * FROM productos WHERE id = ?", (producto_id,))
        producto = cursor.fetchone()
        if not producto:
            return False  # No existe

        # Eliminamos el producto
        cursor.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
        conexion.commit()
        return True

    except sqlite3.DatabaseError as e:
        if conexion:
            conexion.rollback()
        print(f"Error de base de datos, revisar la integridad del archivo {database}")
        sys.exit()

    except sqlite3.Error as e:
        if conexion:
            conexion.rollback()
        print(f"Error al eliminar el producto por ID: {e}")
        return False

    finally:
        if conexion:
            conexion.close()



def obtener_productos_con_stock_bajo(database, limite):
    """
    Devuelve una lista de productos cuya cantidad es menor o igual al límite especificado.
    """
    conexion = None
    productos = []
    try:
        conexion = sqlite3.connect(database)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
        productos = cursor.fetchall()

    except sqlite3.DatabaseError:
        print(f"Error de base de datos, revisar la integridad del archivo {database}")
        sys.exit()

    except sqlite3.Error as e:
        print(f"Error al obtener productos con stock bajo: {e}")

    finally:
        if conexion:
            conexion.close()

    return productos



def main():
    print("main de mod_backend se ejecuta desde el main.py")
if __name__ == '__main__':
    main()
    