from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from conexion.conexion import get_db_connection

app = Flask(__name__)
app.secret_key = "clave_secreta_super_segura"

# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (user_id,))
    user_data = cursor.fetchone()
    cursor.close()
    conn.close()
    if user_data:
        return User(user_data["id_usuario"], user_data["nombre"], user_data["email"], user_data["password"])
    return None

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()

        if user_data and check_password_hash(user_data["password"], password):
            user = User(user_data["id_usuario"], user_data["nombre"], user_data["email"], user_data["password"])
            login_user(user)
            flash("Inicio de sesión exitoso", "success")
            return redirect(url_for("protected"))
        else:
            flash("Credenciales incorrectas", "danger")

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        password = request.form["password"]
        hashed_password = generate_password_hash(password)

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)",
                       (nombre, email, hashed_password))
        conn.commit()
        cursor.close()
        conn.close()

        flash("Usuario registrado con éxito", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/protected")
@login_required
def protected():
    return render_template("protected.html", user=current_user)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Sesión cerrada", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
