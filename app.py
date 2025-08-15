from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return """
    ¡Hola, mundo desde Flask en Linux Lite!<br>
    Jose Luis Maldonado Rodriguez<br>
    Desarrollo de aplicaciones Web - Universidad Estatal Amazónica<br>
    Tecnologías de la Información
    """

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f"""
    Bienvenido, {nombre}!<br>
    José Luis Maldonado Rodríguez<br>
    Desarrollo de aplicaciones Web - Universidad Estatal Amazónica<br>
    Tecnologías de la Información
    """

if __name__ == '__main__':
    app.run(debug=True)
