from flask import Flask, render_template, request, redirect, url_for
from conexion.conexion import crear_conexion

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Crear usuario
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        nombre = request.form['nombre']
        mail = request.form['mail']
        conexion = crear_conexion()
        if conexion:
            cursor = conexion.cursor()
            sql = "INSERT INTO usuarios (nombre, mail) VALUES (%s, %s)"
            cursor.execute(sql, (nombre, mail))
            conexion.commit()
            conexion.close()
            return redirect(url_for('list_users'))
    return render_template('add_user.html')

# Leer usuarios
@app.route('/list_users')
def list_users():
    conexion = crear_conexion()
    usuarios = []
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT id_usuario, nombre, mail FROM usuarios")
        usuarios = cursor.fetchall()
        conexion.close()
    return render_template('list_users.html', usuarios=usuarios)

# Editar usuario
@app.route('/edit_user/<int:id_usuario>', methods=['GET', 'POST'])
def edit_user(id_usuario):
    conexion = crear_conexion()
    if not conexion:
        return "Error al conectar a la base de datos"
    
    cursor = conexion.cursor()
    if request.method == 'POST':
        nombre = request.form['nombre']
        mail = request.form['mail']
        sql = "UPDATE usuarios SET nombre = %s, mail = %s WHERE id_usuario = %s"
        cursor.execute(sql, (nombre, mail, id_usuario))
        conexion.commit()
        conexion.close()
        return redirect(url_for('list_users'))
    
    # Si es GET, obtenemos los datos actuales
    cursor.execute("SELECT id_usuario, nombre, mail FROM usuarios WHERE id_usuario = %s", (id_usuario,))
    usuario = cursor.fetchone()
    conexion.close()
    return render_template('edit_user.html', usuario=usuario)

# Eliminar usuario
@app.route('/delete_user/<int:id_usuario>', methods=['GET', 'POST'])
def delete_user(id_usuario):
    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s", (id_usuario,))
        conexion.commit()
        conexion.close()
    return redirect(url_for('list_users'))
@app.route('/test_db')
def test_db():
    conexion = crear_conexion()
    if conexion:
        conexion.close()
        return "¡Conexión con la base de datos exitosa!"
    else:
        return "Error al conectar a la base de datos."

if __name__ == '__main__':
    app.run(debug=True)
