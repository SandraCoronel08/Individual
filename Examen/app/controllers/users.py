from app import app
import re

from flask import Flask, flash, redirect, render_template, request, session,url_for

from app.models.user import User

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/pantalla')
def pantalla():
    return render_template('pantalla.html')


@app.route('/logout')
def logout():
    session.pop('usuario', None)  # Elimina la sesión del usuario
    return redirect(url_for('inicio'))  # Redirige al inicio


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def inicio():
    return render_template('index.html')

regular = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")

def verificar_correo(correo):
    if re.fullmatch(regular, correo):
        return True
    else:
        return False

@app.route('/registro/',methods=['POST'])
def registro():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo = request.form['correo']
    contrasenha = request.form['contrasenha']
    confirmar_contrasenha = request.form['confirmar_contrasenha']

    if not nombre or not apellido or not correo or not contrasenha or not confirmar_contrasenha:
        return redirect(url_for('inicio'))
    if len(nombre) < 3 or len(apellido) < 3:
        return redirect(url_for('inicio'))
    
    if verificar_correo == False:
        return redirect(url_for('inicio'))

    if len(contrasenha) < 8:
        return redirect(url_for('inicio'))

    if contrasenha != confirmar_contrasenha:
        return redirect(url_for('inicio'))
    
    usuario = User.obtener_por_correo(correo)
    if usuario:
        return redirect(url_for('inicio'))


    hash_contrasenha = bcrypt.generate_password_hash(contrasenha).decode('utf-8')
    datos_usuario = {
        'nombre': nombre,
        'apellido': apellido,
        'correo': correo,
        'contrasenha': hash_contrasenha
    }

    resultado = User.guardar(datos_usuario)

    if resultado:
        print('Se guardo el usuario')
        return redirect(url_for('inicio'))
    else:
        print('No se guardo el usuario')
        return redirect(url_for('inicio'))
    
@app.route('/login/',methods=['POST'])
def login():
    correo = request.form['correo']
    contrasenha = request.form['contrasenha']

    if not correo or not contrasenha:
        return redirect(url_for('inicio'))
    datos = {
        'correo' : correo
    }

    usuario = User.obtener_por_correo(datos)
    if usuario == None:
        return redirect(url_for('inicio'))
    
    if correo == usuario.correo and bcrypt.check_password_hash(usuario.contrasenha, contrasenha):
        session['usuario'] = {
            'id' : usuario.id,
            'nombre' : usuario.nombre,
            'apellido' : usuario.apellido,
            'correo' : usuario.correo
        }
        print('Se logro iniciar sesion')
        return redirect(url_for('pantalla')) 
        
    else:
        print('No se logro iniciar sesion')
        return redirect(url_for('inicio'))
   