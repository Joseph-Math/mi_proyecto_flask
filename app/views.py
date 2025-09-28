from flask import current_app, Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from .db import get_db, close_db
from functools import wraps

def init_views(app):
    app.teardown_appcontext(close_db)
    bp = Blueprint('main', __name__)
    register_routes(bp)
    app.register_blueprint(bp)

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('user_id'):
            return redirect(url_for('main.login'))
        return f(*args, **kwargs)
    return decorated

def register_routes(bp):
    @bp.route('/')
    def index():
        nombres = {
            'universidad': 'Universidad Estatal Amazónica',
            'curso': 'Desarrollo de Aplicaciones Web - Práctico Experimental',
            'autor': 'José Luis Maldonado Rodríguez'
        }
        return render_template('index.html', nombres=nombres)

    @bp.route('/login', methods=['GET','POST'])
    def login():
        if request.method=='POST':
            username = request.form.get('username','').strip()
            password = request.form.get('password','').strip()
            db = get_db()
            cur = db.cursor(dictionary=True)
            cur.execute('SELECT * FROM usuarios WHERE username=%s', (username,))
            user = cur.fetchone()
            if user and check_password_hash(user['password'], password):
                session.clear()
                session['user_id'] = user['id']
                session['username'] = user['username']
                flash('Ingreso exitoso','success')
                return redirect(url_for('main.productos'))
            flash('Usuario o contraseña incorrectos','danger')
        return render_template('login.html')

    @bp.route('/logout')
    def logout():
        session.clear()
        flash('Sesión cerrada','info')
        return redirect(url_for('main.index'))

    @bp.route('/register', methods=['GET','POST'])
    def register():
        if request.method=='POST':
            username = request.form.get('username','').strip()
            password = request.form.get('password','').strip()
            if not username or not password:
                flash('Ingrese usuario y contraseña','warning')
                return redirect(url_for('main.register'))
            db = get_db()
            cur = db.cursor()
            hashed = generate_password_hash(password)
            try:
                cur.execute('INSERT INTO usuarios (username, password) VALUES (%s,%s)', (username, hashed))
                flash('Usuario registrado','success')
                return redirect(url_for('main.login'))
            except Exception as e:
                flash('Error al registrar usuario: '+str(e),'danger')
        return render_template('register.html')

    @bp.route('/productos')
    @login_required
    def productos():
        db = get_db()
        cur = db.cursor(dictionary=True)
        cur.execute('SELECT * FROM productos ORDER BY id_producto DESC')
        productos = cur.fetchall()
        return render_template('productos.html', productos=productos)

    @bp.route('/crear', methods=['GET','POST'])
    @login_required
    def crear():
        if request.method=='POST':
            nombre = request.form.get('nombre','').strip()
            precio = request.form.get('precio','0').strip()
            stock = request.form.get('stock','0').strip()
            errors = []
            if not nombre:
                errors.append('El nombre es requerido.')
            try:
                precio = float(precio)
            except:
                errors.append('Precio inválido.')
            try:
                stock = int(stock)
            except:
                errors.append('Stock inválido.')
            if errors:
                for e in errors:
                    flash(e,'warning')
                return redirect(url_for('main.crear'))
            db = get_db()
            cur = db.cursor()
            cur.execute('INSERT INTO productos (nombre, precio, stock) VALUES (%s,%s,%s)', (nombre, precio, stock))
            flash('Producto creado','success')
            return redirect(url_for('main.productos'))
        return render_template('form_producto.html', accion='Crear', producto=None)

    @bp.route('/editar/<int:id>', methods=['GET','POST'])
    @login_required
    def editar(id):
        db = get_db()
        cur = db.cursor(dictionary=True)
        cur.execute('SELECT * FROM productos WHERE id_producto=%s', (id,))
        producto = cur.fetchone()
        if not producto:
            flash('Producto no encontrado','danger')
            return redirect(url_for('main.productos'))
        if request.method=='POST':
            nombre = request.form.get('nombre','').strip()
            precio = request.form.get('precio','0').strip()
            stock = request.form.get('stock','0').strip()
            errors = []
            if not nombre:
                errors.append('El nombre es requerido.')
            try:
                precio = float(precio)
            except:
                errors.append('Precio inválido.')
            try:
                stock = int(stock)
            except:
                errors.append('Stock inválido.')
            if errors:
                for e in errors:
                    flash(e,'warning')
                return redirect(url_for('main.editar', id=id))
            cur2 = db.cursor()
            cur2.execute('UPDATE productos SET nombre=%s, precio=%s, stock=%s WHERE id_producto=%s', (nombre, precio, stock, id))
            flash('Producto actualizado','success')
            return redirect(url_for('main.productos'))
        return render_template('form_producto.html', accion='Editar', producto=producto)

    @bp.route('/eliminar/<int:id>', methods=['POST'])
    @login_required
    def eliminar(id):
        confirm = request.form.get('confirm','')
        if confirm != 'SI':
            flash('Debe confirmar escribiendo SI para eliminar','warning')
            return redirect(url_for('main.productos'))
        db = get_db()
        cur = db.cursor()
        cur.execute('DELETE FROM productos WHERE id_producto=%s', (id,))
        flash('Producto eliminado','success')
        return redirect(url_for('main.productos'))
