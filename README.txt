# Sistema de Gestión Básica de Productos

Este proyecto es una aplicación de consola escrita en Python que permite gestionar un inventario de productos utilizando una base de datos SQLite. 

Permite realizar operaciones como:

- Agregar productos
- Mostrar productos registrados
- Buscar por nombre o ID
- Actualizar productos
- Eliminar productos
- Reporte de Stock

---

## Estructura del Proyecto

inventario/
│
├── data/
│ └── data.db # Base de datos SQLite (se crea si no existe)
│
├── mod_backend.py # Funciones de acceso a la base de datos
├── mod_frontend.py # Lógica del menú e interacción con el usuario
├── main.py # Programa principal
└── README.txt # Este archivo

La base de datos se crea automáticamente en la carpeta data/ si no existe.

Requisitos
Python 3.7 o superior
SQLite3 (incluido con Python)

Notas Técnicas
La ruta a la base de datos es dinámica: se construye usando os.path.abspath(__file__) para asegurar compatibilidad al ejecutar desde cualquier carpeta.

El archivo main.py se encarga de iniciar el programa y pasar la ruta de la base de datos como parámetro.

El módulo mod_frontend.py gestiona el input del usuario y llama a funciones de mod_backend.py, que se encarga de las operaciones reales en SQLite.

Desarrollado por Javier Alvaredo.