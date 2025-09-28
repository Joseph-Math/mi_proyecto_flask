

<h1>Proyecto Flask</h1>
<p>Este proyecto es un sistema web desarrollado en Flask, con conexión a <strong>MariaDB/MySQL</strong>, diseñado para gestionar usuarios, estudiantes, profesores, cursos, asistencia y calificaciones. El proyecto se desarrolló con un enfoque <strong>modular y escalable</strong>, integrando buenas prácticas de programación web.</p>

<hr>

<h2>Contenido del Proyecto</h2>
<ul>
    <li><code>app.py</code> → Archivo principal de Flask con rutas y controladores.</li>
    <li><code>conexion/</code> → Módulo para la conexión con la base de datos.</li>
    <li><code>usuarios/</code> → Módulo para manejo de usuarios (CRUD).</li>
    <li><code>templates/</code> → Plantillas HTML utilizando <strong>Bootstrap</strong> para diseño responsivo.</li>
    <li><code>static/</code> → Archivos estáticos (CSS, JS, imágenes).</li>
    <li><code>venv/</code> → Entorno virtual de Python.</li>
    <li><code>requirements.txt</code> → Dependencias del proyecto.</li>
</ul>

<hr>

<h2>Tareas por Semana</h2>

<h3>Semana 15: Aplicación CRUD con Flask y MySQL</h3>
<p><strong>Descripción de la Tarea:</strong><br>
Ampliación del proyecto Flask de semanas anteriores, incorporando un sistema <strong>CRUD</strong> (Crear, Leer, Actualizar, Eliminar) conectado a una base de datos <strong>MySQL</strong>. Permite manipular datos desde la interfaz web de manera dinámica. Se incluye el código actualizado y el script SQL de la base de datos.</p>

<h4>Instrucciones y pasos realizados:</h4>
<ul>
    <li><strong>Configuración inicial del proyecto:</strong>
        <ul>
            <li>Crear entorno virtual e instalar Flask.</li>
            <li>Crear la estructura del proyecto (<code>app.py</code>, carpetas <code>templates</code> y <code>static</code>).</li>
            <li>Definir rutas básicas y verificar el funcionamiento.</li>
            <li>Subir proyecto inicial a GitHub.</li>
        </ul>
    </li>
    <li><strong>Base de datos MySQL:</strong>
        <ul>
            <li>Crear base de datos <code>desarrollo_web</code>.</li>
            <li>Crear tabla <code>productos</code> (o tablas necesarias) con campos:
                <ul>
                    <li><code>id_producto</code> (INT, auto incremental, PK)</li>
                    <li><code>nombre</code> (VARCHAR)</li>
                    <li><code>precio</code> (DECIMAL)</li>
                    <li><code>stock</code> (INT)</li>
                </ul>
            </li>
            <li>Instalar conector Python:
                <pre>pip install mysql-connector-python</pre>
            </li>
        </ul>
    </li>
    <li><strong>Implementación del CRUD con Flask:</strong>
        <ul>
            <li>Crear Producto: Ruta <code>/crear</code> para registrar un nuevo producto desde formulario HTML. Validar los datos antes de insertarlos.</li>
            <li>Leer Productos: Ruta <code>/productos</code> para mostrar todos los productos en una tabla HTML.</li>
            <li>Actualizar Producto: Ruta <code>/editar/&lt;id&gt;</code> para editar información de un producto existente.</li>
            <li>Eliminar Producto: Ruta <code>/eliminar/&lt;id&gt;</code> con confirmación antes de eliminar.</li>
        </ul>
    </li>
    <li><strong>Interfaz y Estilo:</strong>
        <ul>
            <li>Uso de plantillas Jinja2 (<code>base.html</code>, <code>formulario.html</code>, etc.).</li>
            <li>Aplicación de estilos con Bootstrap para mejor presentación.</li>
        </ul>
    </li>
    <li><strong>Subida a GitHub:</strong>
        <ul>
            <li>Integración de cambios locales con la versión remota (<code>git pull --rebase</code>).</li>
            <li>Resolución de conflictos en scripts SQL.</li>
            <li>Commit y push final al repositorio.</li>
        </ul>
    </li>
</ul>

<p><strong>Notas adicionales:</strong></p>
<ul>
    <li>Se utilizó hashing de contraseñas con <code>werkzeug.security.generate_password_hash</code>.</li>
    <li>Interfaz base sencilla, ampliable visualmente en futuras versiones.</li>
    <li>CRUD funcional para gestión de productos desde la web.</li>
</ul>

<hr>

<h3>Semana 14: Implementación de sistema de login con Flask y MySQL</h3>
<p><strong>Descripción de la Tarea:</strong><br>
Incorporación de un sistema de login funcional con autenticación de usuarios utilizando Flask-Login y MySQL.</p>

<h4>Instrucciones y pasos realizados:</h4>
<ul>
    <li><strong>Configuración del proyecto Flask:</strong>
        <ul>
            <li>Creación de la estructura del proyecto con <code>app.py</code>.</li>
            <li>Definición de rutas básicas (<code>/</code>, <code>/login</code>, <code>/register</code>, <code>/protected</code>, <code>/logout</code>).</li>
            <li>Verificación del funcionamiento de la aplicación.</li>
            <li>Subida inicial del proyecto a GitHub.</li>
        </ul>
    </li>
    <li><strong>Configuración de MySQL en Flask:</strong>
        <ul>
            <li>Instalación de MySQL en el sistema.</li>
            <li>Creación de la base de datos <code>liceo_policial</code> y tabla <code>usuarios</code> (campos: <code>id_usuario</code>, <code>nombre</code>, <code>email</code>, <code>password</code>).</li>
            <li>Instalación del conector <code>mysql-connector-python</code>.</li>
            <li>Creación de la carpeta <code>conexion</code> y archivo <code>conexion.py</code> para gestionar la conexión.</li>
        </ul>
    </li>
    <li><strong>Implementación del sistema de login:</strong>
        <ul>
            <li>Inicialización de Flask-Login en <code>app.py</code>.</li>
            <li>Definición del modelo de usuario en <code>models.py</code>.</li>
            <li>Función para cargar usuarios desde MySQL.</li>
        </ul>
    </li>
    <li><strong>Registro y autenticación de usuarios:</strong>
        <ul>
            <li>Ruta <code>/register</code> con contraseña hasheada.</li>
            <li>Ruta <code>/login</code> verificando credenciales.</li>
            <li>Ruta <code>/logout</code>.</li>
            <li>Ruta protegida <code>/protected</code>.</li>
        </ul>
    </li>
    <li><strong>Subida a GitHub:</strong>
        <ul>
            <li>Integración de cambios locales con la versión remota.</li>
            <li>Resolución de conflictos en scripts SQL.</li>
            <li>Commit y push final al repositorio.</li>
        </ul>
    </li>
</ul>

<p><strong>Notas adicionales:</strong></p>
<ul>
    <li>Se utilizó hashing de contraseñas con <code>werkzeug.security.generate_password_hash</code>.</li>
    <li>Interfaz base sencilla, ampliable visualmente.</li>
</ul>

<hr>

<h3>Semana 13: Uso de bases de datos relacionales</h3>
<ul>
    <li>Creación de tablas necesarias (usuarios, estudiantes, profesores, cursos, asistencia, calificaciones, roles, logs).</li>
    <li>Consultas básicas de selección, inserción, actualización y eliminación.</li>
    <li>Modularización del código para futuras expansiones.</li>
</ul>

<h3>Semana 12: Persistencia de datos en un entorno local</h3>
<ul>
    <li>Conexión con base de datos MariaDB/MySQL.</li>
    <li>Implementación de CRUD para la tabla usuarios.</li>
    <li>Pruebas de conexión y persistencia local.</li>
</ul>

<h3>Semana 11: Validación de formularios</h3>
<ul>
    <li>Implementación de formularios para creación y edición de usuarios.</li>
    <li>Validación básica de campos en el servidor.</li>
    <li>Manejo de rutas POST y GET.</li>
</ul>

<h3>Semana 10: Plantillas de contenido dinámico y reutilización</h3>
<ul>
    <li>Creación de templates con Jinja2.</li>
    <li>Uso de <code>base.html</code> como plantilla base.</li>
    <li>Integración de Bootstrap para diseño.</li>
</ul>

<h3>Semana 09: Configuración básica de proyecto web</h3>
<ul>
    <li>Inicialización del proyecto Flask.</li>
    <li>Configuración de rutas básicas (<code>/</code>, <code>/test_db</code>).</li>
    <li>Preparación del entorno virtual y gestión de dependencias.</li>
</ul>

<hr>

<h2>Cómo ejecutar el proyecto</h2>
<ol>
    <li>Clonar el repositorio: <code>git clone &lt;URL_DE_TU_REPOSITORIO&gt;</code></li>
    <li>Entrar a la carpeta del proyecto: <code>cd nombre_del_proyecto</code></li>
    <li>Crear entorno virtual e instalar dependencias:
        <pre>
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
        </pre>
    </li>
    <li>Ejecutar la aplicación: <code>python run.py</code></li>
    <li>Abrir navegador y acceder a: <code>http://localhost:5000</code></li>
</ol>

</body>
</html>
