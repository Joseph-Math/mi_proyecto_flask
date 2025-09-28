PROYECTO FLASK

Este proyecto es un sistema web desarrollado en Flask, con conexión a MariaDB/MySQL, diseñado para gestionar usuarios, estudiantes, profesores, cursos, asistencia y calificaciones. El proyecto se desarrolló con un enfoque modular y escalable, integrando buenas prácticas de programación web.

CONTENIDO DEL PROYECTO

app.py → Archivo principal de Flask con rutas y controladores.

conexion/ → Módulo para la conexión con la base de datos.

usuarios/ → Módulo para manejo de usuarios (CRUD).

templates/ → Plantillas HTML utilizando Bootstrap para diseño responsivo.

static/ → Archivos estáticos (CSS, JS, imágenes).

venv/ → Entorno virtual de Python.

requirements.txt → Dependencias del proyecto.

TAREAS POR SEMANA

Semana 15: Aplicación CRUD con Flask y MySQL

Descripción de la Tarea:
Ampliación del proyecto Flask de semanas anteriores, incorporando un sistema CRUD (Crear, Leer, Actualizar, Eliminar) conectado a una base de datos MySQL. Permite manipular datos desde la interfaz web de manera dinámica.
Se incluye el código actualizado y el script SQL de la base de datos.

Instrucciones y pasos realizados:

Configuración inicial del proyecto:

Crear entorno virtual e instalar Flask.

Crear la estructura del proyecto (app.py, carpetas templates y static).

Definir rutas básicas y verificar el funcionamiento.

Subir proyecto inicial a GitHub.

Base de datos MySQL:

Crear base de datos desarrollo_web.

Crear tabla productos (o tablas necesarias de tu proyecto) con campos:

id_producto (INT, auto incremental, PK)

nombre (VARCHAR)

precio (DECIMAL)

stock (INT)

Instalar conector de Python: pip install mysql-connector-python

Implementación del CRUD con Flask:

Crear Producto: Ruta /crear para registrar un nuevo producto desde formulario HTML. Validar los datos antes de insertarlos.

Leer Productos: Ruta /productos para mostrar todos los productos en una tabla HTML.

Actualizar Producto: Ruta /editar/<id> para editar información de un producto existente.

Eliminar Producto: Ruta /eliminar/<id> con confirmación antes de eliminar.

Interfaz y Estilo:

Uso de plantillas Jinja2 (base.html, formulario.html, etc.).

Aplicación de estilos con Bootstrap para mejor presentación.

Subida a GitHub:

Integración de cambios locales con la versión remota (git pull --rebase).

Resolución de conflictos en scripts SQL.

Commit y push final al repositorio.

Notas adicionales:

Se utilizó hashing de contraseñas con werkzeug.security.generate_password_hash.

Interfaz base sencilla, ampliable visualmente en futuras versiones.

CRUD funcional para gestión de productos desde la web.

Semana 14: Implementación de sistema de login con Flask y MySQL

Descripción de la Tarea:
El objetivo de esta semana es que los estudiantes amplíen su proyecto Flask creado en semanas anteriores incorporando un sistema de login funcional con autenticación de usuarios utilizando Flask-Login y MySQL. Además, deberán subir el código actualizado a su repositorio de GitHub junto con el script de la base de datos.

Instrucciones y pasos realizados:

Configuración del proyecto Flask:

Creación de la estructura del proyecto con app.py.

Definición de rutas básicas (/ , /login , /register , /protected , /logout ).

Verificación del funcionamiento de la aplicación.

Subida inicial del proyecto a GitHub.

Configuración de MySQL en Flask:

Instalación de MySQL en el sistema.

Creación de la base de datos liceo_policial y la tabla usuarios (campos: id_usuario, nombre, email, password).

Instalación del conector mysql-connector-python.

Creación de la carpeta conexion y el archivo conexion.py para gestionar la conexión con la base de datos.

Implementación del sistema de login:

Inicialización de Flask-Login en app.py.

Definición del modelo de usuario en models.py.

Función para cargar usuarios desde MySQL.

Registro y autenticación de usuarios:

Ruta para registrar usuarios (/register) con contraseña hasheada.

Ruta para iniciar sesión (/login) verificando credenciales.

Ruta para cerrar sesión (/logout).

Ruta protegida (/protected) accesible solo para usuarios autenticados.

Subida del proyecto actualizado a GitHub:

Integración de cambios locales con la versión remota (git pull --rebase).

Resolución de conflictos en scripts SQL.

Commit y push final al repositorio: https://github.com/Joseph-Math/mi_proyecto_flask.git

Notas adicionales:

Se utilizó hashing de contraseñas con werkzeug.security.generate_password_hash.

La interfaz base se mantiene sencilla, con posibilidad de mejorar visualmente en semanas posteriores.

Semana 13: Uso de bases de datos relacionales: configuración, modelos y consultas básicas

Creación de tablas necesarias (usuarios, estudiantes, profesores, cursos, asistencia, calificaciones, roles, logs).

Consultas básicas de selección, inserción, actualización y eliminación.

Modularización del código para facilitar futuras expansiones.

Semana 12: Persistencia de datos en un entorno local

Conexión con base de datos MariaDB/MySQL.

Implementación de CRUD para la tabla usuarios.

Pruebas de conexión y persistencia local.

Semana 11: Validación de formularios

Implementación de formularios para creación y edición de usuarios.

Validación básica de campos en el lado del servidor.

Manejo de rutas POST y GET para procesamiento de formularios.

Semana 10: Plantillas de generación de contenido dinámico y reutilización de componentes

Creación de templates con Jinja2.

Uso de base.html como plantilla base para reutilizar componentes.

Integración de Bootstrap para mejorar el diseño.

Semana 09: Configuración básica de un proyecto web y manejo de rutas

Inicialización del proyecto Flask.

Configuración de rutas básicas (/ , /test_db ).

Preparación del entorno virtual y gestión de dependencias.

CÓMO EJECUTAR EL PROYECTO

Clonar el repositorio:
git clone <URL_DE_TU_REPOSITORIO>

Entrar a la carpeta del proyecto:
cd nombre_del_proyecto

Crear entorno virtual e instalar dependencias:
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows
pip install -r requirements.txt

Ejecutar la aplicación:
python run.py

Abrir navegador y acceder a:
http://localhost:5000
