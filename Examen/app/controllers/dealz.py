from app import app
from flask import render_template,request,redirect,url_for,session

from app.models.user import User
from app.models.auto import Auto

@app.route('/dashboard')
def dashboard():
    if "usuario" not in session:
        return redirect(url_for("inicio"))
    
    todos = Auto.todos()
    usuario = session["usuario"]
    return render_template("dashboard.html", usuario=usuario, autos=todos)

@app.route('/new')
def new():
    if "usuario" not in session:
        return redirect(url_for("inicio"))
    return render_template("agregar.html")

@app.route('/agregar',methods=["POST"])
def agregar():
    marca = request.form["marca"]
    modelo = request.form["modelo"]
    ingredientes = request.form["ingredientes"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    user_id = session["usuario"]['id']

    if not marca or not modelo or not ingredientes or not descripcion or not precio or not user_id:
        return redirect(url_for("dashboard"))
    datos_vehiculo  = {
        'marca':marca,
        'modelo':modelo,
        'ingredientes':ingredientes,
        'descripcion':descripcion,
        'precio':precio,
        'user_id':user_id
    }
    resultado = Auto.guardar(datos_vehiculo)
    if resultado:
        print(f"Vehiculo agregado {datos_vehiculo['marca']}")
        return redirect(url_for("dashboard"))
    else:
        print("Error al agregar")
        return redirect(url_for("dashboard"))
    
@app.route('/show/<int:id>')
def show(id):
    
    data = {
        'id': id
    }
    show = Auto.uno(data)

    
    return render_template("show.html", show=show)

@app.route('/edit/<int:id>')
def edit(id):
    data = {
        'id': id
    }
    edit = Auto.uno(data)
    return render_template("edit.html", edit=edit)
@app.route('/editar/<int:id>',methods=["POST"])
def editar(id):
    marca = request.form["marca"]
    modelo = request.form["modelo"]
    ingredientes = request.form["ingredientes"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    user = session["usuario"]
    user_id = user["id"]

    if not marca or not modelo or not ingredientes or not descripcion or not precio or not user_id:
        return redirect(url_for("dashboard"))
    datos_vehiculo  = {
        'marca':marca,
        'modelo':modelo,
        'ingredientes':ingredientes,
        'descripcion':descripcion,
        'precio':precio,
        'user_id':user_id,
        'id':id
    }

    editar_vehiculo = Auto.editar(datos_vehiculo)
    if editar_vehiculo:
        print(f"Vehiculo editado {datos_vehiculo['marca']}")
        return redirect(url_for("dashboard"))
    else:
        print("Error al editar")
        return redirect(url_for("dashboard"))

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id':id
    }
    delete = Auto.borrar(data)

    if delete:
        print(f"Vehiculo eliminado {id}")
        return redirect(url_for("dashboard"))
    else:
        print("Error al eliminar")
        return redirect(url_for("dashboard"))
    
    