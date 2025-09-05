from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import os, json, csv, datetime

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATOS_DIR = os.path.join(BASE_DIR, "datos")
DB_PATH = os.path.join(BASE_DIR, "database", "usuarios.db")

# Configuración SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + DB_PATH
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Modelo de usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    creado = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "email": self.email, "creado": self.creado.isoformat()}

# Crear carpetas necesarias
os.makedirs(DATOS_DIR, exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "database"), exist_ok=True)

# Inicializar DB si no existe
with app.app_context():
    if not os.path.exists(DB_PATH):
        db.create_all()

# -------------------
# Rutas principales
# -------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")

@app.route("/guardar", methods=["POST"])
def guardar():
    nombre = request.form.get("nombre")
    email = request.form.get("email")
    if not nombre or not email:
        return render_template("resultado.html", mensaje="Faltan datos")

    registro = {"nombre": nombre, "email": email, "timestamp": datetime.datetime.utcnow().isoformat()}

    # 1) Guardar en TXT
    with open(os.path.join(DATOS_DIR, "datos.txt"), "a", encoding="utf-8") as f:
        f.write(f"{registro['timestamp']} | {nombre} | {email}\n")

    # 2) Guardar en JSON
    json_path = os.path.join(DATOS_DIR, "datos.json")
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        data = []
    next_id = (max([item.get("id",0) for item in data]) + 1) if data else 1
    item = {"id": next_id, "nombre": nombre, "email": email, "timestamp": registro["timestamp"]}
    data.append(item)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # 3) Guardar en CSV
    csv_path = os.path.join(DATOS_DIR, "datos.csv")
    file_exists = os.path.exists(csv_path) and os.path.getsize(csv_path) > 0
    with open(csv_path, "a", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["id","nombre","email","timestamp"])
        writer.writerow([item["id"], nombre, email, item["timestamp"]])

    # 4) Guardar en SQLite
    usuario = Usuario(nombre=nombre, email=email)
    db.session.add(usuario)
    db.session.commit()

    return render_template("resultado.html", mensaje="Guardado en TXT, JSON, CSV y SQLite.")

# -------------------
# Lectura de datos
# -------------------
@app.route("/leer_txt")
def leer_txt():
    path = os.path.join(DATOS_DIR, "datos.txt")
    contenido = ""
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            contenido = f.read()
    return "<pre>" + contenido + "</pre>"

@app.route("/leer_json")
def leer_json():
    path = os.path.join(DATOS_DIR, "datos.json")
    data = []
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    return jsonify(data)

@app.route("/leer_csv")
def leer_csv():
    path = os.path.join(DATOS_DIR, "datos.csv")
    rows = []
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                rows.append(r)
    return jsonify(rows)

@app.route("/listar_db")
def listar_db():
    usuarios = Usuario.query.order_by(Usuario.id.desc()).all()
    return jsonify([u.to_dict() for u in usuarios])

if __name__ == "__main__":
    app.run(debug=True)
