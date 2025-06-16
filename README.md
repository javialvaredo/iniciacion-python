# Sistema de Gestión Básica de Productos

Este proyecto es una aplicación de consola escrita en Python que permite gestionar una lista de productos usando operaciones CRUD (Crear, Leer, Buscar y Eliminar). El programa principal interactúa con un módulo personalizado que contiene todas las funciones necesarias para el manejo de productos.

---

## 📦 Características

- **Agregar productos** con nombre, categoría, precio y fecha/hora de registro.
- **Mostrar productos** en formato legible.
- **Buscar productos** por nombre exacto.
- **Eliminar productos** con confirmación.
- **Interfaz interactiva** por consola con limpieza de pantalla y validaciones.

---

## 🗂 Estructura del Proyecto

```
├── main.py                # Archivo principal del programa
└── modulo_funciones/
    └── funciones.py       # Módulo con funciones auxiliares
```

---

## 📋 Formato de los productos

Cada producto se guarda como una lista con los siguientes elementos:

```python
[nombre, categoría, precio (int), fecha_y_hora_compra (str)]
```

## ✅ Validaciones

- El precio debe ser un número entero.
- No se permiten campos vacíos para nombre o categoría.
- Al eliminar un producto, se solicita confirmación previa.
- Los productos se distinguen por nombre exacto (sensible a mayúsculas/minúsculas iniciales).

---

## 🚀 Cómo ejecutar el programa

1. Asegúrate de tener **Python 3** instalado.
2. Descarga o clona este repositorio.
3. Abre una terminal en la carpeta del proyecto.
4. Ejecuta el archivo principal:

```bash
python main.py
```

---

## 🧪 Ejemplo de uso

```
**************************************
Sistema de Gestión Básica De Productos
**************************************

1. Agregar producto
2. Mostrar productos
3. Buscar producto
4. Eliminar producto
5. Salir
Seleccione una opción: 1
Ingrese nombre de producto: Café
Ingrese categoría: Bebidas
Ingrese el precio (sin centavos): 1500
Producto agregado correctamente.
```

---

## 👨‍💻 Autor

Javier Alvaredo  
Argentina 🇦🇷  
Proyecto educativo de Python para prácticas de CRUD.

---

¡Gracias por probar este sistema de gestión de productos!