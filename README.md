# 📦 Sistema de Gestión Básica de Productos

Este proyecto es una aplicación de consola escrita en Python que permite gestionar un inventario de productos utilizando una base de datos SQLite. 

Permite realizar operaciones como:

- Agregar productos
- Mostrar productos registrados
- Buscar por nombre o ID
- Actualizar productos
- Eliminar productos
- Reporte de Stock

---

## 📁 Estructura del Proyecto

inventario/
│
├── data/
│ └── data.db # Base de datos SQLite (se crea si no existe)
│
├── base_datos.py # Funciones de acceso a la base de datos
├── funciones.py # Lógica del menú e interacción con el usuario
├── main.py # Programa principal
└── README.md # Este archivo

Este proyecto usa colorama para colorear el texto en consola.

La base de datos se crea automáticamente en la carpeta data/ si no existe.

Requisitos
Python 3.7 o superior
SQLite3 (incluido con Python)
Módulo colorama (instalable vía pip)

📂 Notas Técnicas
La ruta a la base de datos es dinámica: se construye usando os.path.abspath(__file__) para asegurar compatibilidad al ejecutar desde cualquier carpeta.

El archivo main.py se encarga de iniciar el programa y pasar la ruta de la base de datos como parámetro.

El módulo funciones.py gestiona el input del usuario y llama a funciones de base_datos.py, que se encarga de las operaciones reales en SQLite.

Desarrollado por Javier Alvaredo.