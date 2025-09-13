# Proyecto Flask: Sistema Liceo Policial

Este proyecto es un sistema web desarrollado en Flask, con conexión a **MariaDB/MySQL**, diseñado para gestionar usuarios, estudiantes, profesores, cursos, asistencia y calificaciones. El proyecto se desarrolló con un enfoque **modular y escalable**, integrando buenas prácticas de programación web.

---

## Contenido del Proyecto

- `app.py` → Archivo principal de Flask con rutas y controladores.
- `conexion/` → Módulo para la conexión con la base de datos.
- `usuarios/` → Módulo para manejo de usuarios (CRUD).
- `templates/` → Plantillas HTML utilizando **Bootstrap** para diseño responsivo.
- `static/` → Archivos estáticos (CSS, JS, imágenes).
- `venv/` → Entorno virtual de Python.
- `requirements.txt` → Dependencias del proyecto.

---

## Tareas por Semana

### Semana 09: Configuración básica de un proyecto web y manejo de rutas
- Inicialización del proyecto Flask.
- Configuración de rutas básicas (`/`, `/test_db`).
- Preparación del entorno virtual y gestión de dependencias.

### Semana 10: Plantillas de generación de contenido dinámico y reutilización de componentes
- Creación de templates con **Jinja2**.
- Uso de `base.html` como plantilla base para reutilizar componentes.
- Integración de Bootstrap para mejorar el diseño.

### Semana 11: Validación de formularios
- Implementación de formularios para creación y edición de usuarios.
- Validación básica de campos en el lado del servidor.
- Manejo de rutas POST y GET para procesamiento de formularios.

### Semana 12: Persistencia de datos en un entorno local
- Conexión con base de datos **MariaDB/MySQL**.
- Implementación de CRUD para la tabla `usuarios`.
- Pruebas de conexión y persistencia local.

### Semana 13: Uso de bases de datos relacionales: configuración, modelos y consultas básicas
- Creación de tablas necesarias (`usuarios`, `estudiantes`, `profesores`, `cursos`, `asistencia`, `calificaciones`, `roles`, `logs`).
- Consultas básicas de selección, inserción, actualización y eliminación.
- Modularización del código para facilitar futuras expansiones.

---

## Cómo ejecutar el proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/Joseph-Math/mi_proyecto_flask.git
cd mi_proyecto_flask
