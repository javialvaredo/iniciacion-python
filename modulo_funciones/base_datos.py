import sqlite3

def get_connection():
    return sqlite3.connect("data/mi_base_de_datos.db")
