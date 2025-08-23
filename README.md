## Semana 9

### Descripción de la Tarea
Configurar un proyecto web básico en **Flask**, definir rutas y almacenar el proyecto en un repositorio de GitHub.  
Esto permitirá a los estudiantes **comprender la estructura básica de Flask** y el manejo de control de versiones.

### Instrucciones

1. **Instalación y Configuración del Proyecto**
   - Crear una carpeta con el nombre `proyecto`.
   - Configurar un entorno virtual (venv):
     ```bash
     python -m venv venv
     .\venv\Scripts\activate   # En Windows
     source venv/bin/activate  # En Linux/Mac
     ```
   - Instalar Flask:
     ```bash
     pip install flask
     ```

2. **Configuración Básica del Proyecto**
   - Estructura inicial:
     ```
     /mi_proyecto_flask
     ├── app.py
     ├── static/
     ├── requirements.txt
     ├── .gitignore
     ```
   - Archivo `app.py` con ruta principal `/`.

   - Verificar aplicación en:
     ```
     http://127.0.0.1:5000/
     ```

3. **Manejo de Rutas**
   - Agregar ruta personalizada para usuario:
     ```python
     @app.route('/usuario/<nombre>')
     def usuario(nombre):
         return f'Bienvenido, {nombre}!'
     ```

---

## Semana 10

### Descripción de la Tarea
Extender el proyecto Flask creado en la semana anterior, integrando **plantillas dinámicas con Jinja2** para mejorar la organización del código y permitir reutilización de componentes.  
Finalmente, actualizar el repositorio en GitHub.

### Instrucciones

1. **Si aún no tienes el proyecto Flask:**
   - Configurar entorno virtual.
   - Instalar Flask.
   - Crear `app.py` y rutas básicas.
   - Subir el proyecto a GitHub.

2. **Extender el Proyecto con Plantillas Dinámicas**
   - Estructura del proyecto:
     ```
     /mi_proyecto_flask
     ├── app.py
     ├── templates/
     │   ├── base.html
     │   ├── index.html
     │   ├── about.html
     ├── static/
     │   ├── styles.css
     ├── requirements.txt
     ├── .gitignore
     ```
   - Modificar `app.py` para usar plantillas.
   - Crear `base.html` como plantilla base.
   - Crear páginas heredadas:
     - `index.html` (inicio).
     - `about.html` (acerca de).

3. **Actualizar el Repositorio en GitHub**
   - Subir cambios con:
     ```bash
     git add .
     git commit -m "Semana 10 - Implementación de plantillas con Jinja2"
     git push origin main
     ```

---

## Tecnologías Utilizadas
- [Python 3.x](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Jinja2](https://jinja.palletsprojects.com/)
- Git & GitHub

---

## Autor
**José Luis Maldonado**  
Licenciado en Ciencias de la Educación, mención en Física y Matemática.  
Estudiante de Ingeniería en Tecnologías de la Información.
