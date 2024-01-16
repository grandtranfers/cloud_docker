from flask import Flask, request, render_template
import logging as log
import mysql.connector

log.basicConfig(level=log.INFO)

app = Flask(__name__)

# Configura la conexion a la base de datos MySQL
db_config = {
    'host': 'mysql', # Definido en el docker-compose en seccion posterior
    'user': 'root',
    'password': 'ejemplo',
    'database': 'mydatabase'
}

def store_data_db(data):
    try:
        # Conecta a la base de datos MySQL
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Inserta los datos en la tabla forms
        cursor.execute("INSERT INTO usuarios (nombre) VALUES (%s);", (data,))

        # Realiza commit y cierra la conexion
        conn.commit()
        conn.close()
        log.info("registrado exitosamente")
    except:
        log.warning("No se pudo insertar en la base de datos %s (Database may not be ready): " %(data))

@app.route('/')
def index():
    # Esta funcion se asocia a la ruta raiz "/"
    return "Bienvenido Luis Angel a mi aplicacion web2!"

@app.route('/formulario', methods=[ 'GET','POST'])
def formulario():
   # Esta funcion se asocia a la ruta "/formulario"
    if request.method == 'POST':
        # Si se envia el formulario, procesamos los datos
        nombre = request.form['nombre']
        #apellido = request.form['apellido']

        # Llama a la funcion para almacenar datos en la base de datos
        store_data_db(nombre)

        mensaje = f"Hola, {nombre}. Bienvenido Luis a mi app web. Esta procesando la base de datos"
        return mensaje
    #Si se accede por GET, mostramos el formulario
    return render_template('formulario.html')

@app.route('/buscador', methods=[ 'GET','POST'])
def buscador():
    try:
        # Esta funcion se asocia a la ruta "/buscador"
        if request.method == 'POST':
            # Si se envia el formulario, procesamos los datos
            nombre = request.form['nombre']
            mensaje = f"Hola, {nombre}. Bienvenido mi pagina de consultas"
            return mensaje
        #Si se accede por GET, mostramos el formulario
        return render_template('buscador.html')
    except:
            log.warning("No se pudo encontrar la pagina buscar.html")
       
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
