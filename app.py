# Importamos Flask y la función render_template para mostrar archivos HTML
from flask import Flask, render_template
import os

# Inicializamos la aplicación Flask
app = Flask(__name__)

# Definimos la ruta principal (la raíz de la página '/')
@app.route('/')
def inicio():
    # Esta función busca automáticamente dentro de la carpeta 'templates'
    return render_template('index.html')

# Bloque obligatorio para arrancar el servidor localmente
if __name__ == '__main__':
    # Leemos el puerto que nos asigne el servidor, o usamos el 5000 por defecto
    puerto = int(os.environ.get("PORT", 5000))
    # Arrancamos la app escuchando en todas las direcciones de red
    app.run(host='0.0.0.0', port=puerto, debug=True)
