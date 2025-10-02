# Proyecto Flask

Este proyecto es un sistema web desarrollado en **Flask**, con conexión a **MariaDB/MySQL**, diseñado para gestionar usuarios, estudiantes, profesores, cursos, asistencia y calificaciones. El proyecto se desarrolló con un enfoque modular y escalable, integrando buenas prácticas de programación web.

---

## Contenido del Proyecto

- `app.py` → Archivo principal de Flask con rutas y controladores.  
- `conexion/` → Módulo para la conexión con la base de datos.  
- `usuarios/` → Módulo para manejo de usuarios (CRUD).  
- `templates/` → Plantillas HTML utilizando Bootstrap para diseño responsivo.  
- `static/` → Archivos estáticos (CSS, JS, imágenes).  
- `venv/` → Entorno virtual de Python.  
- `requirements.txt` → Dependencias del proyecto.  

---

## Tareas por Semana

### Semana 15: Aplicación CRUD con Flask y MySQL
**Descripción:**  
Ampliación del proyecto Flask, incorporando un sistema **CRUD** (Crear, Leer, Actualizar, Eliminar) conectado a una base de datos MySQL. Permite manipular datos desde la interfaz web de manera dinámica.  

**Pasos realizados:**

1. **Configuración inicial**
   - Crear entorno virtual e instalar Flask.
   - Crear estructura del proyecto (`app.py`, carpetas `templates` y `static`).
   - Definir rutas básicas y verificar funcionamiento.
   - Subir proyecto inicial a GitHub.

2. **Base de datos MySQL**
   - Crear base de datos `desarrollo_web`.
   - Crear tabla `productos`:
     ```sql
     id_producto INT AUTO_INCREMENT PRIMARY KEY,
     nombre VARCHAR(255),
     precio DECIMAL(10,2),
     stock INT
     ```
   - Instalar conector Python:
     ```bash
     pip install mysql-connector-python
     ```

3. **Implementación del CRUD**
   - **Crear Producto:** `/crear` → registrar un nuevo producto desde formulario HTML.  
   - **Leer Productos:** `/productos` → mostrar todos los productos en tabla HTML.  
   - **Actualizar Producto:** `/editar/<id>` → editar información de un producto existente.  
   - **Eliminar Producto:** `/eliminar/<id>` → confirmación antes de eliminar.  

4. **Interfaz y Estilo**
   - Uso de plantillas Jinja2 (`base.html`, `formulario.html`, etc.).
   - Aplicación de estilos con Bootstrap.

5. **Subida a GitHub**
   - Integración de cambios locales con la versión remota (`git pull --rebase`).  
   - Resolución de conflictos en scripts SQL.  
   - Commit y push final al repositorio.

**Notas adicionales:**  
- Se utilizó **hashing de contraseñas** con `werkzeug.security.generate_password_hash`.  
- Interfaz base sencilla, ampliable visualmente.  
- CRUD funcional para gestión de productos desde la web.

---

### Semana 14: Sistema de login con Flask y MySQL
**Descripción:**  
Implementación de un sistema de login funcional con autenticación de usuarios utilizando **Flask-Login** y MySQL.  

**Pasos realizados:**

1. **Configuración del proyecto**
   - Crear estructura (`app.py`) y rutas básicas (`/`, `/login`, `/register`, `/protected`, `/logout`).
   - Verificar funcionamiento.
   - Subir proyecto inicial a GitHub.

2. **Configuración de MySQL**
   - Instalación de MySQL en el sistema.
   - Crear base de datos `liceo_policial` y tabla `usuarios`:
     ```sql
     id_usuario INT AUTO_INCREMENT PRIMARY KEY,
     nombre VARCHAR(255),
     email VARCHAR(255),
     password VARCHAR(255)
     ```
   - Instalar conector Python:
     ```bash
     pip install mysql-connector-python
     ```
   - Crear carpeta `conexion` y archivo `conexion.py`.

3. **Implementación del sistema de login**
   - Inicializar Flask-Login en `app.py`.
   - Definir modelo de usuario en `models.py`.
   - Función para cargar usuarios desde MySQL.

4. **Registro y autenticación**
   - `/register` → contraseña hasheada.  
   - `/login` → verificación de credenciales.  
   - `/logout` → cerrar sesión.  
   - `/protected` → ruta protegida.  

5. **Subida a GitHub**
   - Integración de cambios locales con versión remota.
   - Resolución de conflictos en scripts SQL.  
   - Commit y push final: [Repositorio](https://github.com/Joseph-Math/mi_proyecto_flask.git)

**Notas adicionales:**  
- Hashing de contraseñas con `werkzeug.security.generate_password_hash`.  
- Interfaz base sencilla, con posibilidad de mejoras visuales.

---

### Semana 13: Bases de datos relacionales
- Creación de tablas (`usuarios`, `estudiantes`, `profesores`, `cursos`, `asistencia`, `calificaciones`, `roles`, `logs`).  
- Consultas básicas (SELECT, INSERT, UPDATE, DELETE).  
- Modularización del código para futuras expansiones.

### Semana 12: Persistencia de datos en entorno local
- Conexión con MariaDB/MySQL.  
- CRUD para la tabla `usuarios`.  
- Pruebas de conexión y persistencia.

### Semana 11: Validación de formularios
- Formularios para creación y edición de usuarios.  
- Validación básica del lado del servidor.  
- Manejo de rutas POST y GET.

### Semana 10: Plantillas dinámicas y reutilización
- Creación de templates con **Jinja2**.  
- `base.html` como plantilla base.  
- Integración de **Bootstrap**.

### Semana 09: Configuración básica de proyecto web
- Inicialización de Flask.  
- Configuración de rutas básicas (`/`, `/test_db`).  
- Preparación del entorno virtual y gestión de dependencias.

---

## Cómo ejecutar el proyecto

```bash
# Clonar el repositorio
git clone <URL_DE_TU_REPOSITORIO>

# Entrar a la carpeta del proyecto
cd nombre_del_proyecto

# Crear entorno virtual e instalar dependencias
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt

# Ejecutar la aplicación
python run.py
