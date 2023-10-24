from app import app
from app.controllers.users import *
from app.controllers.dealz import *
from flask import send_from_directory

# Aquí se define la ruta para servir archivos estáticos
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == "__main__":
    app.run(debug=True)
